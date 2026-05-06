class CustomException:

    class RepositoryError(Exception):
        pass

    class ServiceError(Exception):
        pass

    class NotFoundError(RepositoryError):
        pass

    class BadRequestException(ServiceError):
        pass