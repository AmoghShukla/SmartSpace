from uuid import UUID

from src.service.floor import FloorService
from src.schema.floor import FloorCreate, FloorResponse, FloorUpdate
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
def CreateFloor(payload : FloorCreate, db : Session = Depends(get_db), user = Depends(required_role(['ADMIN']))):
    try:
        logger.info(f"Creating floor at workspace with workspace_id : {payload.workspace_id}, Floor_Auditorium_Capacity : {payload.floor_auditorium_capacity}, Floor_Meeting_Room_Capacity : {payload.floor_meeting_room_capacity}")
        return FloorService.CreateFloor(payload, db)
    except CustomException.ServiceError as e:
        logger.debug(f"Creating floor at workspace with workspace_id : {payload.workspace_id}, Floor_Auditorium_Capacity : {payload.floor_auditorium_capacity}, Floor_Meeting_Room_Capacity : {payload.floor_meeting_room_capacity}")
        raise HTTPException(status_code=400,detail=str(e))


@router.get('/get_by_floor_id/{Floor_id}', response_model=FloorResponse)
def GetFloorsByFloorID(floor_id : UUID, db : Session = Depends(get_db), user = Depends(required_role(['ADMIN']))):
    try:
        logger.info(f"Fetching floor : {floor_id} ")
        return FloorService.GetFloorByFloorID(floor_id, db)
    except CustomException.ServiceError as e:
        logger.debug(f"Error while Fetching floor ")
        raise HTTPException(status_code=400, detail=str(e))

@router.get('/get_all_by_workspace_id/{workspace_id}', response_model=list[FloorResponse])
def GetAllFloorsWithWorkspaceID(workspace_id : UUID,db : Session = Depends(get_db), user = Depends(required_role(['ADMIN']))):
    try:
        logger.info(f"Fetching all floors with workspace id : {workspace_id}")
        return FloorService.GetAllFloorsByWorkspaceID(workspace_id, db)
    except CustomException.ServiceError as e:
        logger.debug(f"Error while Fetching floor with workspaceID ")
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/getall', response_model=list[FloorResponse])
def GetAllFloors(db : Session = Depends(get_db), user = Depends(required_role(['ADMIN']))):
    try:
        logger.info(f"Fetching all floors across workspaces")
        return FloorService.GetAllFloors(db)
    except CustomException.ServiceError as e:
        logger.debug(f"Error while Fetching floor ")
        raise HTTPException(status_code=400, detail=str(e))


@router.patch('/update_user', response_model=FloorResponse)
def UpdateFloor(payload : FloorUpdate, current_user = Depends(get_current_user), db : Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER']))):
    try:
        logger.info(f"Updating floor with Payload : {payload}")
        return FloorService.UpdateFloor(payload, db)
    except CustomException.ServiceError as e:
        logger.debug(f"Error while Updating Floor with Payload : {payload}")
        raise HTTPException(status_code=400,detail=str(e))

@router.delete('/Make_unavailable', response_model=FloorResponse)
def MakeFloorUnavailable(floor_id : UUID, db : Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER']))):
    try:
        logger.info(f"Making the Floor Unavailable")
        return FloorService.MakeFloorUnavailable(floor_id, db)
    except CustomException.ServiceError as e:
        logger.debug(f"Error while making floor unavailable")
        raise HTTPException(status_code=400, detail=str(e))