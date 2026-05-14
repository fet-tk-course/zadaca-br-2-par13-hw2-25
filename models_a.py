from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import field_validator as validator


# TODO: Student A - Definiši svoj SQLModel entitet ovdje
# 

# CarBase - definira atribute automobila koji su obavezni prilikom kreiranja novog automobila
class CarBase(SQLModel):
    model_name: str
    year: int
    price: float
    is_electric: bool
    mileage: int
    color: str
    description: Optional[str] = None
    manufacturer_id: int = Field(default=1, foreign_key="manufacturer.id")

# Car - koristi se kao model tabele u bazi podataka, nasljeđuje atribute iz CarBase i dodaje id koji je primarni ključ
class Car(CarBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

# CarCreate - koristi se za kreiranje novog automobila, nasljeđuje atribute iz CarBase


class CarCreate(CarBase):
    @validator('model_name')
    @classmethod
    def model_name_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Naziv modela ne smije biti prazan')
        if len(v.strip()) < 2:
            raise ValueError('Naziv modela mora imati najmanje 2 znaka')
        return v

    @validator('price')
    @classmethod
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Cijena mora biti pozitivan broj')
        return v



# Shema za djelimično ažuriranje gdje su sva polja su opcionalna
class CarUpdate(SQLModel):
    model_name: Optional[str] = None
    year: Optional[int] = None
    price: Optional[float] = None
    is_electric: Optional[bool] = None
    mileage: Optional[int] = None
    color: Optional[str] = None
    description: Optional[str] = None
    manufacturer_id: Optional[int] = None

