from library import guid, repr_toString
from constant.enum import PhoneType
from . import Base

@repr_toString
class Phone(Base):  
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, 
                 type: PhoneType = PhoneType.Business, 
                 number: int = None):
        self._id = guid()
        self.type = type
        self.number = number

__all__ = ["Phone"]