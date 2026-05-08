from uuid import UUID

from src.repository.payment import PaymentRepository
from src.repository.booking import BookingRepository
from src.service.payment import PaymentService
# from src.schema.payment import BookingCreate, BookingCreateResponse, BookingUpdateResponse, MyBookingResponse
from src.database.Session import get_db
from src.Exceptions.Custom_Exception import CustomException
from src.dependencies.auth import get_current_user, required_role
from src.utils.loggers import get_logger

from sqlalchemy.orm import Session

from fastapi import APIRouter, HTTPException, Depends

router = APIRouter(prefix="/Payment", tags=['Payment'])
logger = get_logger(__name__)

def Complete_Payment(booking_id, db : Session = Depends(get_db), current_user = Depends(get_current_user), access = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER', 'USER']))):
    try:
        payment = PaymentRepository.GetPaymentByBookingID(booking_id, db)
        if payment.user_id != current_user.user_id:
            return {
                'message' : "Please Enter Your Own Booking_ID"
            }    
    except CustomException.ServiceError as e:
        raise HTTPException(status_code=400, detail={'error' : e}) from e