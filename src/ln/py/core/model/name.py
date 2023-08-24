from library import guid, repr_toString
from constant.enum import Title
from . import Base

@repr_toString
class Name(Base):  
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, 
                 title: Title = Title.Mr, 
                 first: str = str(),
                 middle: str = str(),
                 last: str = str()):
        self._id = guid()
        self.title = title
        self.first = first
        self.middle = middle
        self.last = last

__all__ = ["Name"]