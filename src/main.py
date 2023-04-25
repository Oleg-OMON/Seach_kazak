from urllib.request import Request
from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError
from starlette import status
from starlette.responses import JSONResponse
from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers
from auth.manager import get_user_manager
from auth.auth import auth_backend
from auth.schemas import UserRead, UserCreate
from auth.models import user, User
import sentry_sdk

from kazak.router import router as kazaks_router

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
    tags=["Auth"],
)


app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

current_user = fastapi_users.current_user()

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







