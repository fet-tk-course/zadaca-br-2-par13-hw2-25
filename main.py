from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import create_db_and_tables
from routes_a import router as cars_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title = "Zadaća 2 - REST API",
    description = "REST API za upravljanje automobilima i proizvođačima u auto salonu"
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(cars_router)

@app.get("/")
def read_root():
    return {"message": "Zadaća 2 - REST API"}