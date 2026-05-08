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

