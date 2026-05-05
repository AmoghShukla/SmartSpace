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
def CreateBooking(resource_ids : list[UUID],payload : BookingCreate, db : Session = Depends(get_db), current_user = Depends(get_current_user)):
    try:
        logger.info(f"Creating booking with Payload : {payload}")
        return BookingService.CreateBooking(current_user, resource_ids, payload, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Booking with Payload : {payload}")
        raise HTTPException(status_code=400, detail="Error While Booking!!!") from e

@router.get('/get_booking_by_user_id', response_model=list[BookingCreateResponse])
def GetBookingsByUserID(user_id : UUID, db : Session = Depends(get_db)):
    try:
        logger.info(f"Fetching booking with User_ID : {user_id}")
        return BookingService.GetBookingsByUserID(user_id, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Fetching Booking with user_id : {user_id}")
        raise HTTPException(status_code=400, detail="Error While Fetching Booking!!!") from e

@router.get('/get_booking_by_resource_id', response_model=list[BookingCreateResponse])
def GetBookingsByResourceID(resource_id : UUID, db : Session = Depends(get_db)):
    try:
        logger.info(f"Fetching booking with Resource_id : {resource_id}")
        return BookingService.GetBookingsByResourceID(resource_id, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Fetching Booking with resource_id : {resource_id}")
        raise HTTPException(status_code=400, detail="Error While Fetching Booking!!!") from e