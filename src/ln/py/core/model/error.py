from library import guid, repr_toString

@repr_toString
class Error():  
    
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, 
                 code: int = 200,
                 message: str = str()):
        self.id = guid()
        self.code = code
        self.message = message

__all__ = ["Error"]