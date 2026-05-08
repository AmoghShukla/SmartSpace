from src.model.enum import PaymentStatus
from src.repository.payment import PaymentRepository
from src.Exceptions.Custom_Exception import CustomException


class PaymentService:

    @staticmethod
    def Complete_Payment(booking_id, db):
        try:
            payment = PaymentRepository.GetPaymentByBookingID(booking_id, db)
            payment.payment_status = PaymentStatus.COMPLETED
            return PaymentRepository.Complete_Payment(payment, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError(e)