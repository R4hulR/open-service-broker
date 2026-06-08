from sqlmodel import SQLModel,create_engine,Field,Session
from fastapi import Depends
from typing import Annotated


class ServiceInstance(SQLModel,table=True):
    instance_id:str|None = Field(default=None,primary_key=True)
    service_id:str
    plan_id:str
    container_id:str
    status:str
    port : str

DATABASE_URL = "postgresql+psycopg2://postgres:password@localhost:5433/mydb"
engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]