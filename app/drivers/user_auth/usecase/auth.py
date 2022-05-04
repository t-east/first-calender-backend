import abc
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from typing import Optional

from sqlalchemy.orm import Session

from app.drivers.user_auth.entity.auth import UserAuth, TokenData
from app.drivers.user_auth.driver.init_data import fake_users_db
from app.drivers.user_auth.jwt_secret_data import SECRET_KEY, ALGORITHM
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class IAuthRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def authenticate_user(self, fake_db, username: str, password: str):
        raise NotImplementedError

class AuthUsecase:
    repo: IAuthRepository

    def __init__(self, repo: IAuthRepository) -> None:
        self.repo = repo

    def _verify_password(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)


    def get_password_hash(self, password: str) -> str:
        return pwd_context.hash(password)


    def _get_user(self, db: Session, username: str) -> Optional[UserAuth]:
        if username in self.db:
            user_dict = db[username]
            return UserAuth(**user_dict)


    def authenticate_user(self, fake_db, username: str, password: str) -> Optional[UserAuth]:
        user = self._get_user(fake_db, username)
        if not user:
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username",
            headers={"WWW-Authenticate": "Bearer"},
        )
        if not self._verify_password(password, user.hashed_password):
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        return user


    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt


    async def get_current_user(self, token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = TokenData(username=username)
        except JWTError:
            raise credentials_exception
        user = self._get_user(fake_users_db, username=token_data.username)
        if user is None:
            raise credentials_exception
        return user
