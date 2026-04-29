from enum import Enum

class UserRole(Enum):
    MEMBER = "MEMBER"
    USER = "USER"
    ADMIN = "ADMIN"
    RESOURCE_MANAGER = "RESOURCE_MANAGER"
    
    