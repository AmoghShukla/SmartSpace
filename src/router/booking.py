from uuid import UUID

from src.service.booking import BookingService
from src.schema.booking import BookingCreate, BookingCreateResponse, BookingUpdateResponse
from src.database.Session import get_db
from src.Exceptions.Custom_Exception import CustomException
from src.dependencies.auth import get_current_user, required_role
from src.utils.loggers import get_logger

from sqlalchemy.orm import Session
from pydantic import EmailStr

from fastapi import APIRouter, HTTPException, Depends

router = APIRouter(prefix="/Booking", tags=['Booking'])
logger = get_logger(__name__)

@router.post('/create_booking', response_model=list[BookingCreateResponse])
def CreateBooking(resource_ids : list[UUID],payload : BookingCreate, db : Session = Depends(get_db), current_user = Depends(get_current_user), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER', 'USER', 'MEMBER']))):
    try:
        logger.info(f"Creating booking with Payload : {payload}")
        return BookingService.CreateBooking(current_user, resource_ids, payload, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Booking with Payload : {payload}")
        raise HTTPException(status_code=400, detail="Error While Booking!!!") from e

@router.get('/get_booking_by_user_id', response_model=list[BookingCreateResponse])
def GetBookingsByUserID(user_id : UUID, db : Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER']))):
    try:
        logger.info(f"Fetching booking with User_ID : {user_id}")
        return BookingService.GetBookingsByUserID(user_id, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Fetching Booking with user_id : {user_id}")
        raise HTTPException(status_code=400, detail="Error While Fetching Booking!!!") from e

@router.get('/get_booking_by_resource_id', response_model=list[BookingCreateResponse])
def GetBookingsByResourceID(resource_id : UUID, db : Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER']))):
    try:
        logger.info(f"Fetching booking with Resource_id : {resource_id}")
        return BookingService.GetBookingsByResourceID(resource_id, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Fetching Booking with resource_id : {resource_id}")
        raise HTTPException(status_code=400, detail="Error While Fetching Booking!!!") from e
    
@router.get('/get_booking_by_workspace_id', response_model=list[BookingCreateResponse])
def GetBookingsByWorkspaceID(workspace_id : UUID, db : Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER']))):
    try:
        logger.info(f"Fetching booking with Workspace_id : {workspace_id}")
        return BookingService.GetBookingsByWorkspaceID(workspace_id, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Fetching Booking with workspace_id : {workspace_id}")
        raise HTTPException(status_code=400, detail="Error While Fetching Booking!!!") from e
    
@router.get('/get_booking_by_floor_id', response_model=list[BookingCreateResponse])
def GetBookingsByFloorID(floor_id : UUID, db : Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER']))):
    try:
        logger.info(f"Fetching booking with Floor id : {floor_id}")
        return BookingService.GetBookingsByFloorID(floor_id, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Fetching Booking with Floor_ID : {floor_id}")
        raise HTTPException(status_code=400, detail="Error While Fetching Booking!!!") from e
    
@router.get('/get_all_bookings', response_model=list[BookingCreateResponse])
def GetAllBookings(db : Session = Depends(get_db), user = Depends(required_role(['ADMIN']))):
    try:
        logger.info(f"Fetching all bookings ")
        return BookingService.GetAllBookings(db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Fetching all the Booking ")
        raise HTTPException(status_code=400, detail="Error While Fetching all Bookings!!!") from e

@router.post('/approve_booking/{booking_id}')
def approve_booking(booking_id : UUID, current_user = Depends(get_current_user), db : Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER']))):
    try:
        return BookingService.approve_booking(booking_id, current_user["user_id"], db)
    except CustomException.ServiceError as e:
        raise HTTPException(status_code=405, detail=e)
    except CustomException.BadRequestException as e:
        raise HTTPException(status_code=400, detail=e)
    except CustomException.NotFoundError as e:
        raise HTTPException(status_code=404, detail=e)

@router.patch('/update_Booking', response_model=BookingCreateResponse)
def UpdateBooking(booking_id : UUID, payload : BookingUpdateResponse, db : Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER', 'MEMBER']))):
    try:
        logger.info(f"Updating booking with Payload : {payload}")
        return BookingService.UpdateBooking(booking_id, payload, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Updating Booking with Booking_ID : {booking_id}")
        raise HTTPException(status_code=400, detail="Error While Updating Booking!!!") from e
    
@router.delete('/Cancel_Booking')
def CancelBooking(booking_id : UUID, db : Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER', 'MEMBER']))):
    try:
        logger.info(f"Cancelling the Booking by Booking ID : {booking_id}")
        return BookingService.Cancel_Booking(booking_id, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Cancelling the Booking By id {booking_id}")
        raise HTTPException(status_code=400, detail=f"Error while Cancelling the Booking By id {booking_id}")
    
@router.delete('/Delete_Booking')
def Hard_Delete_Booking(booking_id : UUID, db : Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER']))):
    try:
        logger.info(f"Delete the Booking by Booking ID : {booking_id}")
        return BookingService.Hard_Delete_Booking(booking_id, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Deleting the Booking By id {booking_id}")
        raise HTTPException(status_code=400, detail=f"Error while CancellinDeletingg the Booking By id {booking_id}")