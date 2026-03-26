<<<<<<< HEAD
from enum import Enum

class GroupNames(Enum):
    ADMIN = "Admin"
    CUSTOMER = "Customer"
    
    @classmethod
    def values(cls):
        """Return all enum values as a list"""
        return [group.value for group in cls]
    
    
=======
from enum import Enum
>>>>>>> ce7ff0aa79a7e51858c9c11b447a1d16de7bd2c0
