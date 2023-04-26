from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from database import get_async_session
from fastapi_cache.decorator import cache
from .models import kazak
from .schemas import Kazak

router = APIRouter(
    prefix='/kazaks',
    tags=["Kazaks"]
)


@router.get("/get_kazak/", response_model=list[Kazak])
@cache(expire=60)
async def get_kazak(city: str, session: AsyncSession = Depends(get_async_session),):
    try:
        query = select(kazak).where(kazak.c.city == city)
        result = await session.execute(query)
        return result.all()


    except Exception:
        HTTPException(status_code=400, detail={
            'status': "error",
            'data': None,
            'details': 'Вы ввели неверные данные!Проверте поля ввода и повторите попытку.'
        })


