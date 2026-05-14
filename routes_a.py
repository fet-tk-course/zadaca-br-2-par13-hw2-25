from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy import func
from sqlmodel import Session, select
from typing import List, Optional

from database import get_session
from models_a import Car, CarCreate, CarUpdate

router = APIRouter(prefix="/cars", tags=["Cars"])

@router.get("/statistics")
def get_cars_statistics(session: Session = Depends(get_session)):
    cars = session.exec(select(Car)).all()    
    if not cars:
        return {
            "ukupno_automobila": 0,
            "prosjecna_cijena": 0.0,
            "prosjecna_kilometraza": 0.0
        }
    
    ukupno = len(cars)
    suma_cijena = sum(car.price for car in cars)
    suma_kilometraze = sum(car.mileage for car in cars)
    
    return {
        "ukupno_automobila": ukupno,
        "prosjecna_cijena": round(suma_cijena / ukupno, 2),
        "prosjecna_kilometraza": round(suma_kilometraze / ukupno, 1)
    }

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


# Ovaj metod služi za upisivanje novog automobila u bazu sa provjerom duplikata
@router.post("/", response_model=Car, status_code=status.HTTP_201_CREATED)
def create_car(car_data: CarCreate, session: Session = Depends(get_session)):
    statement = select(Car).where(
        Car.model_name == car_data.model_name,
        Car.year == car_data.year
    )
    existing_car = session.exec(statement).first()
    if existing_car:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Automobil '{car_data.model_name}' iz {car_data.year}. godine već postoji u bazi podataka."
        )
    car = Car.model_validate(car_data)
    session.add(car)
    session.commit()
    session.refresh(car)
    return car

# Metoda koja se koristi za potpunu zamjenu stanja postojećeg resursa
@router.put("/{car_id}", response_model=Car)
def update_car(car_id: int, car_data: CarCreate, session: Session = Depends(get_session)):
    car = session.get(Car, car_id)
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Automobil nije pronađen")
    car_dict = car_data.model_dump()
    for key, value in car_dict.items():
        setattr(car, key, value)
    session.add(car)
    session.commit()
    session.refresh(car)
    return car

# Metoda koja implementira parcijalne modifikacije
@router.patch("/{car_id}", response_model=Car)
def partial_update_car(car_id: int, car_data: CarUpdate, session: Session = Depends(get_session)):
    car = session.get(Car, car_id)
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Automobil nije pronađen")
    car_dict = car_data.model_dump(exclude_unset=True)
    for key, value in car_dict.items():
        setattr(car, key, value)
    session.add(car)
    session.commit()
    session.refresh(car)
    return car

# Osigurava trajno uklanjanje resursa
@router.delete("/{car_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_car(car_id: int, session: Session = Depends(get_session)):
    car = session.get(Car, car_id)
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Automobil nije pronađen")
    session.delete(car)
    session.commit()

    