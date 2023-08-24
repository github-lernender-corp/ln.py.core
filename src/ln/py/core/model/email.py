from library import guid, repr_toString
from constant.enum import EmailType
from . import Base

@repr_toString
class Email(Base):  
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, 
                 type: EmailType = EmailType.Business, 
                 address: str = str()):
        self._id = guid()
        self.type = type
        self.address = address

__all__ = ["Email"]