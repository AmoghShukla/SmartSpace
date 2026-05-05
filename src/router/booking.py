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
        return BookingService.CreateBooking(resource_ids, payload, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Booking with Payload : {payload}")
        raise HTTPException(status_code=400, detail="Error While Booking!!!") from e