from library import guid, repr_toString
from . import Base

@repr_toString
class Item(Base):  
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self):
        self._id = guid()

__all__ = ["Item"]