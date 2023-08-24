from library import guid, repr_toString
from constant.enum import Direction
from . import Base

@repr_toString
class Sort(Base):  
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, 
                 dir: Direction = Direction.Ascending):
        self._id = guid()
        self.dir = dir

    def isUndefined(self):
        return self.dir == Direction.Undefined

    def isAscending(self):
        return not self.isUndefined() and self.dir == Direction.Ascending
    
    def isDescending(self):
        return not self.isUndefined() and self.dir == Direction.Descending
            
    def toggle(self):       
        if not self.isUndefined():
            if self.dir == Direction.Ascending:
                self.dir = Direction.Descending
            elif self.dir == Direction.Descending:
                self.dir = Direction.Ascending
             
        return self.dir
    
__all__ = ["Sort"]