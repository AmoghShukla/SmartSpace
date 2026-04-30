from uuid import UUID

from src.service.floor import FloorService
from src.schema.floor import FloorCreate, FloorResponse
from src.database.Session import get_db
from src.Exceptions.Custom_Exception import CustomException
from src.dependencies.auth import get_current_user, required_role
from src.utils.loggers import get_logger

from sqlalchemy.orm import Session
from pydantic import EmailStr

from fastapi import APIRouter, HTTPException, Depends

router = APIRouter(prefix="/Floor", tags=['Floor'])
logger = get_logger(__name__)

@router.post('/create_floor', response_model=FloorResponse)
def CreateFloor(workspace_id : UUID, db : Session = Depends(get_db)):
    try:
        logger.info(f"Creating floor at workspace with workspace_id : {workspace_id}")
        return FloorService.CreateFloor(workspace_id, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Creating floor with workpace id : {workspace_id}")
        raise HTTPException(status_code=400, detail="Error While Creating Floor!!!") from e

@router.get('/{workspace_id}', response_model=list[FloorResponse])
def GetAllFloors(workspace_id : UUID, db : Session = Depends(get_db)):
    try:
        logger.info(f"Fetching floor at workspace {workspace_id} ")
        return FloorService.GetAllFloorsByWorkspaceID(db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Fetching floor ")
        raise HTTPException(status_code=400, detail=f"Error While fetching Floor at workspace id : {workspace_id}!!!") from e





@router.get('/all', response_model=list[FloorResponse])
def GetAllFloors(db : Session = Depends(get_db)):
    try:
        logger.info(f"Fetching floor at workspace ")
        return FloorService.GetAllFloorsByWorkspaceID(db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Fetching floor ")
        raise HTTPException(status_code=400, detail="Error While fetching Floor!!!") from e


