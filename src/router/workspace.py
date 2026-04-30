from src.repository.workspace import UserRepository
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
def CreateUser(payload : WorkspaceCreate, db : Session = Depends(get_db)):
    try:
        logger.info(f"Creating workspace with Payload : {payload}")
        return ServiceWorkspace.CreateWorkspace(payload, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Creating workspace with Payload : {payload}")
        raise HTTPException(status_code=400, detail="Error While Creating workspace!!!") from e
    
@router.post('/create_member', response_model=UserResponse)
def CreateMember(payload : MemberCreate, db : Session = Depends(get_db)):
    try:
        logger.info(f"Creating member with Payload : {payload}")
        UserService.CreateUser(payload, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Creating member with Payload : {payload}")
        raise HTTPException("Error While Creating member!!!") from e
    
@router.post('/create_resource_manager', response_model=UserResponse)
def CreateResourceManager(payload : ResourceManagerCreate, db : Session = Depends(get_db)):
    try:
        logger.info(f"Creating resource manager with Payload : {payload}")
        UserService.CreateUser(payload, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Creating resource manager with Payload : {payload}")
        raise HTTPException("Error While Creating resource manager!!!") from e
    
    
@router.get('/get_my_profile', response_model=UserResponse)   
def GetMyProfile(db: Session = Depends(get_db), current_user = Depends(get_current_user), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER', "USER", 'MEMBER']))):
    try:
        logger.info(f"Fetching user Profile")
        return UserService.GetMyProfile(current_user['user_id'],db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while fetching user Profile")
        raise HTTPException("Error While Fetching User Profile!!!") from e

@router.get('/get_user_by_email/{user_email}', response_model=UserResponse)   
def GetUserByEmail(user_email : EmailStr, db: Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER']))):
    try:
        logger.info(f"Fetching user with email : {user_email}")
        return UserService.GetUserByEmail(user_email, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error While Fetching user with email : {user_email}")
        raise HTTPException("Error While Fetching User!!!") from e

@router.get('/get_user_by_role/{user_role}', response_model=UserResponse)  
def GetUserByRole(user_role, db: Session = Depends(get_db), user = Depends(required_role(['ADMIN']))):
    try:
        logger.info(f"Fetching users with role : {user_role}")
        return UserService.GetUserByRole(user_role.upper(), db)
    except CustomException.ServiceError as e:
        logger.error(f"Error users with role : {user_role}")
        raise HTTPException("Error While Fetching User!!!") from e

@router.get('/', response_model=list[UserResponse])    
def GetAllUsers(db: Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER']))):
    try:
        logger.info(f"Fetching All users")
        return UserService.GetAllUsers(db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Fetching users")
        raise HTTPException(status_code=401, detail=str(e))
    
@router.patch('/update_user', response_model=UpdateUser)
def UpdateSelfProfile(payload : UpdateUser, current_user = Depends(get_current_user), db : Session = Depends(get_db)):
    try:
        user = UserService.GetMyProfile(current_user['user_id'],db)
        logger.info(f"Updating user with Payload : {payload}")
        return UserService.UpdateUser(user, payload, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Updating User with Payload : {payload}")
        raise HTTPException(status_code=400,detail="Error While Updating User!!!") from e