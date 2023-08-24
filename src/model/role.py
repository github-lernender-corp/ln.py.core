from library import guid
from . import Base

class Role(Base):  
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, 
                 name: str = str()):
        self._id = guid()
        self.name = name

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

__all__ = ["Role"]