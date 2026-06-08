from fastapi import FastAPI
from app.api.v2 import catalog,instance
from app.db.database import create_db_and_tables
from contextlib import asynccontextmanager
app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
app = FastAPI(lifespan=lifespan)
    
app.include_router(catalog.router)
app.include_router(instance.router)
@app.get("/")
def root():
    return {"message":"Welcome to OSB"}