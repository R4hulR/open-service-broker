from pydantic import BaseModel

class Binding(BaseModel):
    service_id : str
    plan_id: str