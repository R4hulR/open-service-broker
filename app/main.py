from fastapi import FastAPI
from app.api.v2 import catalog
app = FastAPI()

app.include_router(catalog.router)
@app.get("/")
def root():
    return {"message":"Welcome to OSB"}