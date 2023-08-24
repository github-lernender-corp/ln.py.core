from library import (guid, init)
from . import Base
  
class Card(Base):  
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, obj: object):
        self._id = guid()
        self.canCheck = init(obj, 'canCheck', False)
        self.canDelete = init(obj, 'canDelete', False)
        self.checked = init(obj, 'checked', False)
        self.data = init(obj, 'data', {})
        self.canCheck = init(obj, 'canCheck', False)

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

__all__ = ["Card"]