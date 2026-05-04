from src.service.resource import ResourceService
from src.schema.resource import ResourceCreateRegister, ResourceResponse, UpdateResource
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
def CreateWorkspace(payload : ResourceCreateRegister, db : Session = Depends(get_db)):
    try:
        logger.info(f"Creating resource with Payload : {payload}")
        return ResourceService.CreateResource(payload, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Creating Resource with Payload : {payload}")
        raise HTTPException(status_code=400, detail="Error While Creating Resource!!!") from e
'''
@router.get('/get_by_floor_id/{floor_id}', response_model=ResourceResponse)
def GetallAvailableResourcesByFloorID(floor_id,  db):
        try:
            return ResourceRepository.GetallAvailableResourcesByFloorID(floor_id, db)
        except CustomException.ServiceError as e:
            raise CustomException.RepositoryError("Error While Getting Resource") from e'''