from src.service.workspace import WorkspaceService
from src.schema.workspace import WorkspaceCreate, WorkspaceResponse
from src.database.Session import get_db
from src.Exceptions.Custom_Exception import CustomException
from src.dependencies.auth import get_current_user, required_role
from src.utils.loggers import get_logger

from sqlalchemy.orm import Session
from pydantic import EmailStr

from fastapi import APIRouter, HTTPException, Depends

router = APIRouter(prefix="/Workspace", tags=['Workspace'])
logger = get_logger(__name__)

@router.post('/create_workspace', response_model=WorkspaceResponse)
def CreateWorkspace(payload : WorkspaceCreate, db : Session = Depends(get_db), user = Depends(required_role(['ADMIN']))):
    try:
        logger.info(f"Creating workspace with Payload : {payload}")
        return WorkspaceService.CreateWorkspace(payload, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Creating workspace with Payload : {payload}")
        raise HTTPException(status_code=400, detail="Error While Creating workspace!!!") from e

@router.get('/get_workspace_by_name', response_model=WorkspaceResponse)
def GetWorkspaceByName(workspace_name : str, db : Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER', 'USER', 'MEMBER']))):
    try:
        logger.info(f"Getting workspace with Name : {workspace_name}")
        return WorkspaceService.GetWorkspaceByName(workspace_name, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Fetching workspace with Name : {workspace_name}")
        raise HTTPException(status_code=400, detail="Error While Getting workspace!!!") from e
    
@router.get('/get_workspace_by_location', response_model=WorkspaceResponse)
def GetWorkspaceByLocation(workspace_location : str, db : Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER', 'USER', 'MEMBER']))):
    try:
        logger.info(f"Getting workspace with location : {workspace_location}")
        return WorkspaceService.GetWorkspaceByLocation(workspace_location, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Fetching workspace with Name : {workspace_location}")
        raise HTTPException(status_code=400, detail="Error While Getting workspace!!!") from e

@router.get('/get_workspace_by_id', response_model=WorkspaceResponse)
def GetWorkspaceByID(workspace_id : str, db : Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER', 'USER', 'MEMBER']))):
    try:
        logger.info(f"Getting workspace with id : {workspace_id}")
        return WorkspaceService.GetWorkspaceByLocation(workspace_id, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Fetching workspace with id : {workspace_id}")
        raise HTTPException(status_code=400, detail="Error While Getting workspace!!!") from e
        

@router.get('/get_all_workspaces', response_model=list[WorkspaceResponse])
def GetAllWorkSpaces(db : Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER', 'USER', 'MEMBER']))):
    try:
        logger.info(f"Getting all workspaces")
        return WorkspaceService.GetAllWorkspaces(db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Fetching workspaces")
        raise HTTPException(status_code=400, detail="Error While Getting workspaces!!!") from e
    
@router.delete('/Soft_Delete', response_model=WorkspaceResponse)
def Delete(workspace_id : str, db : Session = Depends(get_db), user = Depends(required_role(['ADMIN']))):
    try:
        logger.info(f"Deleting Workspace with id : {workspace_id}")
        return WorkspaceService.SoftDeleteWorkspace(workspace_id, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Deleting Workspace with id : {workspace_id}")
        raise HTTPException(status_code=400, detail=f"Error While Deleting Workspace with id : {workspace_id}!!!") from e
    
@router.delete('/Hard_Delete', response_model=WorkspaceResponse)
def Hard_Delete(workspace_id : str, db : Session = Depends(get_db), user = Depends(required_role(['ADMIN']))):
    try:
        logger.info(f"Deleting Workspace with id : {workspace_id}")
        return WorkspaceService.HardDeleteWorkspace(workspace_id, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Deleting Workspace with id : {workspace_id}")
        raise HTTPException(status_code=400, detail=f"Error While Deleting Workspace with id : {workspace_id}!!!") from e