import json
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from fastapi_cache.decorator import cache
from .models import kazak
from .schemas import Kazak
from fastapi_cache.coder import JsonCoder

router = APIRouter(
    prefix='/kazaks',
    tags=["Kazaks"]
)


@router.get("/get_kazak/")
@cache(expire=60)
async def get_kazak(city: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(kazak).where(kazak.c.city == city)
        ansew = await session.execute(query)
        return {
            "status": "success",
            "data": [r._mapping for r in ansew.all()],
            "details": None
        }



    except Exception:
        HTTPException(status_code=400, detail={
            'status': "error",
            'data': None,
            'details': 'Вы ввели неверные данные!Проверте поля ввода и повторите попытку.'
        })


