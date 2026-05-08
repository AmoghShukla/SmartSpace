from src.model.enum import PaymentStatus
from src.repository.payment import PaymentRepository
from src.Exceptions.Custom_Exception import CustomException
from src.utils.loggers import get_logger

logger = get_logger(__name__)

class PaymentService:

    @staticmethod
    def Complete_Payment(booking_id, db):
        try:
            logger.info(f"Completing Payment for Booking ID : {booking_id}")
            payment = PaymentRepository.GetPaymentByBookingID(booking_id, db)
            logger.info(f"Fetched Payment for Booking ID : {booking_id} with payment ID : {payment.payment_id}")
            payment.payment_status = PaymentStatus.COMPLETED
            return PaymentRepository.Complete_Payment(payment, db)
        except CustomException.RepositoryError as e:
            logger.error(f'Error in Service Layer while Completing Payment with Booking Id : {booking_id} ')
            raise CustomException.ServiceError(e)