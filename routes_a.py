from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List, Optional

from database import get_session
from models_a import Car, CarCreate, CarUpdate

router = APIRouter(prefix="/cars", tags=["Cars"])

# Ovaj metod služi za pregled svih automobila koji su na stanju u salonu
@router.get("/", response_model=List[Car])
def get_cars(
    year: Optional[int] = Query(default=None, description="Filtriranje po godini proizvodnje"),
    is_electric: Optional[bool] = Query(default=None, description="Filtriranje po tipu pogona"),
    session: Session = Depends(get_session)):
    query = select(Car)
    if year is not None:
        query = query.where(Car.year == year)
    if is_electric is not None:
        query = query.where(Car.is_electric == is_electric)
    cars = session.exec(query).all()
    return cars


# Ovaj metod traži jedan specifičan automobil na osnovu njegovog jedinstvenog broja
@router.get("/{car_id}", response_model=Car)
def get_car(car_id: int, session: Session = Depends(get_session)):
    car = session.get(Car, car_id)
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Automobil nije pronađen")
    return car


# Ovaj metod služi za upisivanje novog automobila u bazu
@router.post("/", response_model=Car, status_code=status.HTTP_201_CREATED)
def create_car(car_data: CarCreate, session: Session = Depends(get_session)):
    car = Car.model_validate(car_data)
    session.add(car)
    session.commit()
    session.refresh(car)
    return car