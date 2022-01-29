from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import Optional, List

import app.domains.entities as entities
import app.usecases as usecases
from app.drivers.api.deps import get_user_usecase

router = APIRouter()


@router.post("/", response_model=entities.User)
async def create_user(
    *,
    user_in: entities.UserCreate,
    uu: usecases.UserUsecase = Depends(get_user_usecase)
) -> entities.User:
    return uu.create(obj_in=user_in)


@router.post("/login", response_model=entities.User)
async def login_user(
    *, auth_in: entities.UserAuth, uu: usecases.UserUsecase = Depends(get_user_usecase)
) -> entities.User:
    logined_user: Optional[entities.User] = uu.authenticate(auth_in=auth_in)
    if logined_user is None:
        raise HTTPException(status_code=404)
    return logined_user


@router.put("/", response_model=entities.User)
async def update_user(
    *,
    id: int,
    user_in: entities.UserUpdate,
    uu: usecases.UserUsecase = Depends(get_user_usecase)
) -> entities.User:
    updated_user: Optional[entities.User] = uu.update(id=id, obj_in=user_in)
    if updated_user is None:
        raise HTTPException(status_code=404)
    return updated_user


@router.delete("/{id}", response_model=entities.User)
async def delete_user(
    *, id: int, uu: usecases.UserUsecase = Depends(get_user_usecase)
) -> entities.User:
    deleted_user: Optional[entities.User] = uu.delete(id=id)
    if deleted_user is None:
        raise HTTPException(status_code=404)
    return deleted_user


@router.get("/{id}", response_model=entities.User)
async def get_user(
    *, id: int, uu: usecases.UserUsecase = Depends(get_user_usecase)
) -> entities.User:
    user: Optional[entities.User] = uu.read(id=id)
    if user is None:
        raise HTTPException(status_code=404)
    return user

@router.get("/", response_model=entities.User)
async def get_all_user(
    *, uu: usecases.UserUsecase = Depends(get_user_usecase)
) -> entities.User:
    user: List[Optional[entities.User]] = uu.read_all()
    return user

