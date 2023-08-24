from library import guid
from . import Base

class Item(Base):  
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self):
        self._id = guid()

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

__all__ = ["Item"]