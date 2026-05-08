from sqlmodel import SQLModel, Field
from typing import Optional


class ManufacturerBase(SQLModel):
    name: str
    country: str
    founded_year: int
    employees: int
    is_active: bool
    annual_revenue: float
    website: Optional[str] = None


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