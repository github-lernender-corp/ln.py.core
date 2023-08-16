"""library
This module is designed to encapsulate common functionality used
by developers into a common library.
"""
import uuid
 
def guid() -> str:
    """guid
    This function creates a standard guid
    Returns:
        str: Guid
    """
    _guid = str(uuid.uuid4())
    _guid = _guid.upper()
    return _guid
   
def isNull(o) -> bool:
    """isNull
    Test if a string is null or not
    Returns:
        str: Guid
    """
    if "".__eq__(o):
        True
    
    return False

def hasLength(o) -> bool:
    """hasLength
    Test if a string has length
    Returns:
        str: Guid
    """
    if not isNull(o):
        return len(o) >= 0
    
    return False