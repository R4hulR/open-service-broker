from pydantic import BaseModel

class Instance(BaseModel):
    service_id: str
    plan_id: str