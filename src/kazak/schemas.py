from pydantic import BaseModel


class Kazak(BaseModel):
    id: int
    first_name: str
    last_name: str
    middle_name: str | None = None
    year: str | None = None
    fond: str | None = None
    rang: str | None = None
    city_out: str | None = None
    city: str | None = None
    info_db: str | None = None
    info: str | None = None
    user_id: int | None = None

    class Config:
        orm_mode = True