from fastapi import APIRouter,HTTPException,Response
from app.db.database import SessionDep,ServiceInstance
from app.models.bindings import Binding
router = APIRouter(
    prefix="/v2/service_instances"
)

@router.put("/{instance_id}/service_bindings/{binding_id}")
def bindService(instance_id:str,binding_id:str,binding:Binding,session:SessionDep):
    #checks for an instance with the given instance id
    instance =session.get(ServiceInstance,instance_id)
    if not instance:
        #if it doesn't exist, it throws an 404
        raise HTTPException(status_code=404,detail=f'The instance:{instance_id} doesnt exist')
    return{
        #else it return a dummy credential
        "credentials":{
            "host":"localhost",
            "port":instance.port
        }
    }

@router.delete("/{instance_id}/service_bindings/{binding_id}")
def unbindService(instance_id:str,binding_id:str,session:SessionDep):
    instance = session.get(ServiceInstance,instance_id)
    if not instance:
        raise HTTPException(status_code=404,detail=f'The instance: {instance_id} doesnt exist')
    return Response(status_code=200)