from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlmodel import Session, select
from typing import Optional, List

from database import get_session
from models_b import Manufacturer, ManufacturerCreate, ManufacturerUpdate

router = APIRouter(prefix="/resursi_b", tags=["Resurs B"])

@router.post("/", response_model=Manufacturer, status_code=status.HTTP_201_CREATED)
def create_manufacturer(manufacturer_data: ManufacturerCreate, session: Session = Depends(get_session)):
     postoji=session.exec(select(Manufacturer).where(Manufacturer.name==manufacturer_data.name)).first()

    if postoji:
       raise
HTTPException(status_code=409,detail="Proizvođač već postoji")

    # Kreira novog proizvođača u bazi podataka i vraća kreirani objekat
    manufacturer = Manufacturer.model_validate(manufacturer_data)
    session.add(manufacturer)
    session.commit()
    session.refresh(manufacturer)
    return manufacturer

@router.get("/{manufacturer_id}", response_model=Manufacturer)
def get_manufacturer(manufacturer_id: int, session: Session = Depends(get_session)):
    # Dohvata jednog proizvođača prema ID-u, vraća 404 ako ne postoji
    manufacturer = session.get(Manufacturer, manufacturer_id)
    if not manufacturer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proizvođač nije pronađen")
    return manufacturer

@router.get("/", response_model=List[Manufacturer])
def get_manufacturers(
    country: Optional[str] = Query(default=None, description="Filtriranje po državi porijekla"),
    is_active: Optional[bool] = Query(default=None, description="Filtriranje po aktivnosti na tržištu"),
    session: Session = Depends(get_session)
):
    # Dohvata listu svih proizvođača, sa opcionim filterima po državi i statusu
    query = select(Manufacturer)
    if country is not None:
        query = query.where(Manufacturer.country == country)
    if is_active is not None:
        query = query.where(Manufacturer.is_active == is_active)
    manufacturers = session.exec(query).all()
    return manufacturers

@router.put("/{manufacturer_id}", response_model=Manufacturer)
def update_manufacturer(
    manufacturer_id: int,
    manufacturer_data: ManufacturerCreate,
    session: Session = Depends(get_session)
):
    # Potpuno zamjenjuje podatke proizvođača sa novim podacima (PUT)
    manufacturer = session.get(Manufacturer, manufacturer_id)
    if not manufacturer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proizvođač nije pronađen")
    manufacturer_dict = manufacturer_data.model_dump()
    for key, value in manufacturer_dict.items():
        setattr(manufacturer, key, value)
    session.add(manufacturer)
    session.commit()
    session.refresh(manufacturer)
    return manufacturer

@router.patch("/{manufacturer_id}", response_model=Manufacturer)
def partial_update_manufacturer(
    manufacturer_id: int,
    manufacturer_data: ManufacturerUpdate,
    session: Session = Depends(get_session)
):
    # Djelimično ažurira proizvođača — mijenja samo ona polja koja su proslijeđena
    manufacturer = session.get(Manufacturer, manufacturer_id)
    if not manufacturer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proizvođač nije pronađen")
    manufacturer_dict = manufacturer_data.model_dump(exclude_unset=True)
    for key, value in manufacturer_dict.items():
        setattr(manufacturer, key, value)
    session.add(manufacturer)
    session.commit()
    session.refresh(manufacturer)
    return manufacturer

@router.delete("/{manufacturer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_manufacturer(manufacturer_id: int, session: Session = Depends(get_session)):
    # Briše proizvođača iz baze prema ID-u, vraća 204 bez sadržaja ako uspije
    manufacturer = session.get(Manufacturer, manufacturer_id)
    if not manufacturer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proizvođač nije pronađen")
    session.delete(manufacturer)
    session.commit()