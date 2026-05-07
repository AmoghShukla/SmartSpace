from uuid import UUID

from src.service.resource import ResourceService
from src.schema.resource import ResourceCreateRegister, ResourceResponse, SecondResource, UpdateResource
from src.database.Session import get_db
from src.Exceptions.Custom_Exception import CustomException
from src.dependencies.auth import get_current_user, required_role
from src.utils.loggers import get_logger

from sqlalchemy.orm import Session
from pydantic import EmailStr

from fastapi import APIRouter, HTTPException, Depends

router = APIRouter(prefix="/Resource", tags=['Resource'])
logger = get_logger(__name__)

@router.post('/create_resource', response_model=ResourceResponse)
def CreateResource(payload : ResourceCreateRegister, db : Session = Depends(get_db), user = Depends(required_role(['ADMIN']))):
    try:
        logger.info(f"Creating resource with Payload : {payload}")
        return ResourceService.CreateResource(payload, db)
    except CustomException.ServiceError as e:
        print(e)
        logger.error(f"Error while Creating Resource with Payload : {payload}")
        raise HTTPException(status_code=400, detail="Error While Creating Resource!!! : Router") from e

@router.get('/get_by_all_available_resource_by_id/{floor_id}', response_model=list[ResourceResponse])
def GetallAvailableResourcesByFloorID(page_no : int, floor_id,  db : Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER', 'USER', 'MEMBER']))):
    try:
        logger.info(f"Fetching the resource with Floor ID : {floor_id}")
        return ResourceService.GetallAvailableResourcesByFloorID(page_no, floor_id, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Fetching the resource with Floor ID : {floor_id}")
        raise HTTPException(status_code=400, detail="Error While Getting all the Resources by Floor ID's") from e
    
@router.get('/get_by_resource_by_id/{floor_id}', response_model=list[ResourceResponse])
def GetallAvailableResourcesByWorkspaceID(page_no : int, workspace_id,  db : Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER', 'USER', 'MEMBER']))):
    try:
        logger.info(f"Fetching the resource with Floor ID : {workspace_id}")
        return ResourceService.GetallAvailableResourcesByWorkspaceID(page_no, workspace_id, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Fetching the resource with Floor ID : {workspace_id}")
        raise HTTPException(status_code=400, detail="Error While Getting all the Resources by Workspace ID's") from e

@router.get('/get_by_resource_by_id/{floor_id}', response_model=list[ResourceResponse])
def GetResourcesbyBookingID(page_no : int, workspace_id,  db : Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER', 'USER', 'MEMBER']))):
    try:
        logger.info(f"Fetching the resource with Floor ID : {workspace_id}")
        return ResourceService.GetallAvailableResourcesByWorkspaceID(page_no, workspace_id, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Fetching the resource with Floor ID : {workspace_id}")
        raise HTTPException(status_code=400, detail="Error While Getting all the Resources by Workspace ID's") from e


@router.get('/get_all_resources', response_model=list[ResourceResponse])
def GetallResource(db : Session = Depends(get_db), user = Depends(required_role(['ADMIN']))):
    try:
        logger.info(f"Fetching the resources")
        return ResourceService.GetallResource(db)
    except CustomException.ServiceError as e:
        raise HTTPException(status_code=400, detail=f"Eror while fetching all the Resources") from e

@router.get('/get_resource_by_d/{resource_id}', response_model=ResourceResponse)
def GetResourceByID(resource_id : UUID, db : Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER']))):
    try:
        logger.info(f"Fetching the resources by resource ID : {resource_id}")
        return ResourceService.GetResourceByID(resource_id, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while fetching the Resources By id {resource_id}")
        raise HTTPException(status_code=400, detail=f"Error while fetching the Resources By id {resource_id}")

@router.patch('/Update_price/{resource_id}', response_model=ResourceResponse )
def UpdatePriceByResourceID(resource_id : UUID, new_price : SecondResource, db : Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER']))):
    try:
        logger.info(f"Updating the price of resource with Resource DI : {resource_id}")
        return ResourceService.Change_Resource_Costing(resource_id, new_price, db)
    except CustomException.ServiceError as e:
        raise HTTPException(status_code=400, detail=e)

@router.patch('/get_resource_by_id/{resource_id}', response_model=ResourceResponse)
def UpdateResource(resource_id : UUID, payload : UpdateResource, db : Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER', 'USER', 'MEMBER']))):
    try:
        logger.info(f"Updating the resources by resource ID : {resource_id}")
        return ResourceService.UpdateResource(resource_id, payload, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Updating the Resources By id {resource_id}")
        raise HTTPException(status_code=400, detail=f"Error while Updating the Resources By id {resource_id}")
    
@router.delete('/soft_delete/{resource_id}')
def soft_delete_resource_by_ID(resource_id : UUID, db : Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER']))):
    try:
        logger.info(f"Deleting the resources by resource ID : {resource_id}")
        return ResourceService.soft_delete_resource_by_ID(resource_id, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Deleting the Resources By id {resource_id}")
        raise HTTPException(status_code=400, detail=f"Error while Deleting the Resources By id {resource_id}")

@router.delete('/hard_delete/{resource_id}')
def hard_delete_resource_by_ID(resource_id : UUID, db : Session = Depends(get_db), user = Depends(required_role(['ADMIN']))):
    try:
        logger.info(f"Deleting the resources by resource ID : {resource_id}")
        return ResourceService.hard_delete_resource_by_ID(resource_id, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Deleting the Resources By id {resource_id}")
        raise HTTPException(status_code=400, detail=f"Error while Deleting the Resources By id {resource_id}")