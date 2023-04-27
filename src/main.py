from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError
from starlette import status
from starlette.responses import JSONResponse
from fastapi import FastAPI, Depends
from auth.base_config import auth_backend, fastapi_users, current_user
from auth.schemas import UserRead, UserCreate
from auth.models import user, User
from starlette.requests import Request
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from kazak.router import router as kazaks_router
import sentry_sdk
sentry_sdk.init(
    dsn="https://567aacf038da4b62a6a2c13b4b13c665@o4505046481502208.ingest.sentry.io/4505046484451328",
    traces_sample_rate=1.0,
)

app = FastAPI()


@app.on_event("startup")
async def startup():
    redis = await aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")





app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Auth"],
)


app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)


app.include_router(kazaks_router)





@app.get('/protected-route')
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )







