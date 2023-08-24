from library import guid
from constant.enum import EmailType
from . import Base

class Email(Base):  
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, 
                 type: EmailType, 
                 address: str = str()):
        self._id = guid()
        self.type = type
        self.address = address

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

__all__ = ["Email"]