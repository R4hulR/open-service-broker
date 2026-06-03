from pydantic import BaseModel
from typing import List


class ServicePlan(BaseModel):
    id:str
    name:str
    description: str
    

class Service(BaseModel):
    id:str #An identifier used to correlate this Service Offering in future requests to the Service Broker.
    name:str #The name of the Service Offering. 
    description: str #A short description of the service. MUST be a non-empty string.
    bindable: bool #Specifies whether Service Instances of the service can be bound to applications
    plans: List[ServicePlan]

class CatalogResponse(BaseModel):
    services: List[Service]
