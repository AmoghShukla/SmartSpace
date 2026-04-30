from enum import Enum

class UserRole(Enum):
    MEMBER = "MEMBER"
    USER = "USER"
    ADMIN = "ADMIN"
    WORKSPACE_MANAGER = "WORKSPACE_MANAGER"

class ResourceType(Enum):
    MEETING_ROOM = "MEETING_ROOM"
    AUDITORIUMN = "AUDITORIUMN"
    
    