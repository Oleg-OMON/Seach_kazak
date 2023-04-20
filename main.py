from typing import List
from urllib.request import Request
from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError
from starlette import status
from starlette.responses import JSONResponse
from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from auth.manager import get_user_manager
from auth.auth import auth_backend
from auth.schemas import UserRead, UserCreate
from model import user, kazak
import sentry_sdk

sentry_sdk.init(
    dsn="https://567aacf038da4b62a6a2c13b4b13c665@o4505046481502208.ingest.sentry.io/4505046484451328",
    traces_sample_rate=1.0,
)
app = FastAPI()


fastapi_users = FastAPIUsers[user, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)


app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )







