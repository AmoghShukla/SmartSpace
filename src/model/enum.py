from enum import Enum

class UserRole(Enum):
    MEMBER = "MEMBER"
    USER = "USER"
    ADMIN = "ADMIN"
    WORKSPACE_MANAGER = "WORKSPACE_MANAGER"

class ResourceType(Enum):
    MEETING_ROOM = "MEETING_ROOM"
    AUDITORIUM = "AUDITORIUM"
    
class BookingStatus(str, Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    CANCELLED = "CANCELLED"

class PaymentStatus(str, Enum):
    COMPLETED = "COMPLETED"
    PENDING = "PENDING"
    