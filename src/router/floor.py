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
def CreateFloor(payload : FloorCreate, db : Session = Depends(get_db)):
    try:
        logger.info(f"Creating floor at workspace with workspace_id : {payload.workspace_id}, Floor_Auditorium_Capacity : {payload.floor_auditorium_capacity}, Floor_Meeting_Room_Capacity : {payload.floor_meeting_room_capacity}")
        return FloorService.CreateFloor(payload, db)
    except CustomException.ServiceError as e:
        logger.error(f"Creating floor at workspace with workspace_id : {payload.workspace_id}, Floor_Auditorium_Capacity : {payload.floor_auditorium_capacity}, Floor_Meeting_Room_Capacity : {payload.floor_meeting_room_capacity}")
        raise HTTPException(status_code=400, detail="Error While Creating Floor!!!") from e

@router.get('/{workspace_id}', response_model=list[FloorResponse])
def GetFloorsByWorkspaceID(workspace_id : UUID, db : Session = Depends(get_db)):
    try:
        logger.info(f"Fetching floor at workspace {workspace_id} ")
        return FloorService.GetAllFloorsByWorkspaceID(workspace_id, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Fetching floor ")
        raise HTTPException(status_code=400, detail=f"Error While fetching Floor at workspace id : {workspace_id}!!!") from e


@router.get('/all', response_model=list[FloorResponse])
def GetAllFloors(db : Session = Depends(get_db)):
    try:
        logger.info(f"Fetching floor at all workspaces ")
        return FloorService.GetAllFloors(db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Fetching floor ")
        raise HTTPException(status_code=400, detail="Error While fetching Floor!!!") from e


