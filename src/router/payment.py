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

@router.put('/Complete_payment')
def Complete_Payment(booking_id, db : Session = Depends(get_db), current_user = Depends(get_current_user), access = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER', 'USER']))):
    try:
        logger.info(f"Intiating Payment for Bookign Id : {booking_id}")
        payment = PaymentRepository.GetPaymentByBookingID(booking_id, db)
        if str(payment.user_id) == str(current_user['user_id']):
            return PaymentService.Complete_Payment(booking_id, db)
        else: 
            return {
                'message' : "Please Enter Your Own Booking_ID"
            }
           
    except CustomException.ServiceError as e:
        logger.error("Encountered Error while Completing Payment")
        raise HTTPException(status_code=400, detail={'error' : e}) from e