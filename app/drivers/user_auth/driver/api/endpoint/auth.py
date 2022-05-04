from fastapi import APIRouter, Depends, HTTPException, status
from app.drivers.user_auth.driver.init_data import fake_users_db
from app.drivers.user_auth.jwt_secret_data import ACCESS_TOKEN_EXPIRE_MINUTES
from app.drivers.user_auth.usecase.auth import AuthUsecase as au
from app.drivers.user_auth.entity.auth import Token
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

router = APIRouter()


@router.post("/", response_model=Token)
async def login_for_access_token(user_in: OAuth2PasswordRequestForm = Depends()):
    user = au.authenticate_user(fake_users_db, user_in.username, user_in.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = au.create_access_token(
        data={"sub": user.user_name}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
