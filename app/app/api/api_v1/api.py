from fastapi import APIRouter, Depends
from app.api.deps import create_session
from app.api.api_v1.endpoints import user_auth, user

api_router = APIRouter()

api_router.include_router(user_auth.router, prefix='/auth', tags=['auth'])
api_router.include_router(user.router, prefix='/user', tags=['user'])
