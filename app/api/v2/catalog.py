from fastapi import APIRouter
from app.models.catalog import CatalogResponse,Service,ServicePlan
from typing import List
router = APIRouter(
    prefix="/v2/catalog"
)

Redis1 = ServicePlan(id="1",name="default",description="Default Redis Plan")

Services = Service(id="1",name="redis",description="A redis instance",bindable=True,plans=[Redis1])



@router.get("/")
def getCatalog():
    return CatalogResponse(services=[Services])