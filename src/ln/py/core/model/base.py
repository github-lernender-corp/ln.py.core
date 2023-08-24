
from library import guid, repr_toString

@repr_toString
class Base:  
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, 
                 id: int = None, 
                 name: str = str(), 
                 description: str = str(), 
                 label: str = str(), 
                 active: bool = True, 
                 disabled: bool = False,
                 hidden: bool = False):
        self._id = guid()
        self.id = id
        self.name = name
        self.description = description
        self.label = label
        self.active = active
        self.disabled = disabled
        self.hidden = hidden

__all__ = ["Base"]