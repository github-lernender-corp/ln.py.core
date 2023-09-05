
from library import guid, repr_toString, isArrayWithLength
from model import Error

@repr_toString
class Response:  
    
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, 
                 data: list = [], 
                 errors: list = []):
        self._id = guid()
        self.data = data
        self.errors = errors
        self.total = 0
        
        if (self.hasData(self.data)):
            self.total = len(self.data)

    def hasErrors(self) -> bool:
        return isArrayWithLength(self.errors);

    def hasData(self) -> bool:
        return isArrayWithLength(self.data);
    
__all__ = ["Response"]