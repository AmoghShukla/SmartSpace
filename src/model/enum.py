from enum import Enum

class UserRole(Enum):
    MEMBER = "MEMBER"
    GUEST = "GUEST"
    USER = "USER"
    ADMIN = "ADMIN"
    RESOURCE_MANAGER = "RESOURCE_MANAGER"
    
    