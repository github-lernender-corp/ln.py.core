from library import guid, repr_toString
from . import Base

@repr_toString
class Role(Base):  
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, 
                 name: str = str()):
        self._id = guid()
        self.name = name

__all__ = ["Role"]