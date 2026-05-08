from sqlmodel import SQLModel, Field
from typing import Optional

# TODO: Student A - Definiši svoj SQLModel entitet ovdje
# 

class CarBase(SQLModel):
    model_name: str
    year: int
    price: float
    is_electric: bool
    mileage: int
    color: str
    description: Optional[str] = None
    manufacturer_id: int = Field(default=1, foreign_key="manufacturer.id")

