from src.repository.user import UserRepository
from src.Exceptions.Custom_Exception import CustomException

class UserService:

    def CreateUser(Payload, db):
        try:
            UserRepository.CreateUser(Payload, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError(f"Error Encountered while creating user wit payload {Payload}") from e
        