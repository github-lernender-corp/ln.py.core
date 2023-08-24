from library import guid
from constant.enum import Title
from . import Base

class Name(Base):  
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, 
                 title: Title, 
                 first: str = str(),
                 middle: str = str(),
                 last: str = str()):
        self._id = guid()
        self.title = title
        self.first = first
        self.middle = middle
        self.last = last

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

__all__ = ["Name"]