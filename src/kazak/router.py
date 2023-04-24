from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import kazak
from database import get_async_session

router = APIRouter(
    prefix='/kazaks',
    tags=["Kazaks"]
)


@router.get("/get_kazak")
async def get_kazak(city: str, session: AsyncSession = Depends(get_async_session)):
    query = select(kazak).where(kazak.c.city == city)
    result = await session.execute(query)
    print(result.all())
    return result.all()
