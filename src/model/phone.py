from library import guid
from constant.enum import PhoneType
from . import Base

class Phone(Base):  
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, 
                 type: PhoneType, 
                 number: int = None):
        self._id = guid()
        self.type = type
        self.number = number

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

__all__ = ["Phone"]