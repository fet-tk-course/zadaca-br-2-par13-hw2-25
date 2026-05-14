from sqlmodel import SQLModel, Field
from typing import Optional
from pydentic import field_validator

class ManufacturerBase(SQLModel):
    name: str
    country: str
    founded_year: int
    employees: int
    is_active: bool
    annual_revenue: float
    website: Optional[str] = None
    
    @field_validator('name')
    @classmethod
    def naziv_ne_smije_biti_prazan(cls, v):
        if not v.strip():
            raise ValueError('Naziv ne smije biti prazan string')
        return v.strip()

    @field_validator('employees')
    @classmethod
    def broj_zaposlenih_mora_biti_pozitivan(cls, v):
        if v < 0:
            raise ValueError('Broj zaposlenih ne može biti negativan')
        return v

class Manufacturer(ManufacturerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class ManufacturerCreate(ManufacturerBase):
    pass


class ManufacturerUpdate(SQLModel):
    name: Optional[str] = None
    country: Optional[str] = None
    founded_year: Optional[int] = None
    is_active: Optional[bool] = None
    annual_revenue: Optional[float] = None
    website: Optional[str] = None
    employees: Optional[int] = None