from fastapi import APIRouter,Response
from app.models.instance import Instance
from app.db.database import SessionDep,ServiceInstance
from app.services.docker_service import provision_container,deprovision_container

router = APIRouter(
    prefix="/v2/service_instances"
)

@router.put("/{instance_id}")
def provision_instance(instance_id:str,instance:Instance,session:SessionDep):
    existing = session.get(ServiceInstance,instance_id)
    if existing:
        return {"message":"ok"}
    container_id, port = provision_container(instance_id)
    db_instance = ServiceInstance(**instance.model_dump(),instance_id=instance_id,container_id=container_id,status="Running",port=port)
    session.add(db_instance)
    session.commit()
    session.refresh(db_instance)
    return Response(status_code=201)

@router.delete("/{instance_id}")
def deprovision_instance(instance_id:str,service_id:str,plan_id:str,session:SessionDep):
    existing = session.get(ServiceInstance,instance_id)
    if not existing:
        return Response(status_code=404)
    if existing.service_id == service_id and existing.plan_id==plan_id:
        if deprovision_container(existing.container_id):
            session.delete(existing)
            session.commit()
            return Response(status_code=200)
        else:
            return Response(status_code=500)
    return Response(status_code=422)