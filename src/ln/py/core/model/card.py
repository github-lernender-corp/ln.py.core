from library import (guid, init, repr_toString)
from . import Base

@repr_toString
class Card(Base):  
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, obj: object = None):
        self._id = guid()
        self.canCheck = init(obj, 'canCheck', False)
        self.canDelete = init(obj, 'canDelete', False)
        self.checked = init(obj, 'checked', False)
        self.data = init(obj, 'data', {})
        self.canCheck = init(obj, 'canCheck', False)

__all__ = ["Card"]