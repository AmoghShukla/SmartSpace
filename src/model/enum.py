from enum import Enum

class UserRole(Enum):
    MEMBER = "MEMBER"
    USER = "USER"
    ADMIN = "ADMIN"
    WORKSPACE_MANAGER = "WORKSPACE_MANAGER"
    
    