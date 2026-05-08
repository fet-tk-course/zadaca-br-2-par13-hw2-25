from sqlmodel import SQLModel, Field
from typing import Optional

# TODO: Student B - Definiši svoj SQLModel entitet ovdje
# 
class ManufacturerBase(SQLModel):
    name: str
    country: str
    founded_year: int
    is_active: bool
    annual_revenue: float
    website: Optional[str] = None
    employees: int  

class Manufacturer(ManufacturerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class ManufacturerCreate(ManufacturerBase):
    # Shema za kreiranje novog proizvođača — ne sadrži ID
    pass

class ManufacturerUpdate(SQLModel):
    # Shema za djelimično ažuriranje — sva polja su opcionalna
    name: Optional[str] = None
    country: Optional[str] = None
    founded_year: Optional[int] = None
    is_active: Optional[bool] = None
    annual_revenue: Optional[float] = None
    website: Optional[str] = None
    employees: Optional[int] = None