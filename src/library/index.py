"""library
This module is designed to encapsulate common functionality used
by developers into a common library.
"""
import uuid
import numpy as np
import datetime

def guid() -> str:
    """guid
    This function creates a standard guid
    Returns:
        str: Guid
    """
    _guid = str(uuid.uuid4())
    _guid = _guid.upper()
    return _guid

def isNone(o) -> bool:
    """isUndefined
    Determines if an object is defined
    Returns:
        bool
    """
    return o is None
   
def isNull(o) -> bool:
    """isNull
    Test if a string is null or not
    Returns:
        bool
    """
    return not isNone(o) and "".__eq__(o)

def hasLength(o) -> bool:
    """hasLength
    Test if a string has length
    Returns:
        int
    """
    return not isNull(o) and len(o) >= 0

def isDefined(o) -> bool:
    """isDefined
    Determines if an object is defined
    Returns:
        bool
    """
    return not isNull(o)

def isObject(o) -> bool:
    """isObject
    Determines if a variable is an object
    Returns:
    bool
    """
    return not isNone(o) and isinstance(o, object)

def isInt(o) -> bool:
    """isInt
    Determines if a variable is an object
    Returns:
    bool
    """
    return not isNone(o) and isinstance(o, int)

def isList(o) -> bool:
    """isList
    Determines if a variable is an object
    Returns:
    bool
    """
    return not isNone(o) and isinstance(o, list)

def isFloat(o) -> bool:
    """isFloat
    Determines if a variable is an float
    Returns:
    bool
    """
    return not isNone(o) and isinstance(o, float)

def isComplex(o) -> bool:
    """isComplex
    Determines if a variable is an complex
    Returns:
    bool
    """
    return not isNone(o) and isinstance(o, complex)

def isBool(o) -> bool:
    """isFloat
    Determines if a variable is an boolean
    Returns:
    bool
    """
    return not isNone(o) and isinstance(o, bool)

def isString(o) -> bool:
    """isString
    Determines if a variable is an boolean
    Returns:
    bool
    """
    return not isNone(o) and isinstance(o, str)

def isDict(o) -> bool:
    """isDict
    Determines if a variable is an dictionary
    Returns:
    bool
    """
    return not isNone(o) and isinstance(o, dict)

def isSet(o) -> bool:
    """isSet
    Determines if a variable is an set
    Returns:
    bool
    """
    return not isNone(o) and isinstance(o, set)

def isTuple(o) -> bool:
    """isTuple
    Determines if a variable is an tuple
    Returns:
    bool
    """
    return not isNone(o) and isinstance(o, tuple)

def isRange(o) -> bool:
    """isRange
    Determines if a variable is an range
    Returns:
    bool
    """
    return not isNone(o) and isinstance(o, range)

def isBytes(o) -> bool:
    """isBite
    Determines if a variable is an bytes
    Returns:
    bool
    """
    return not isNone(o) and isinstance(o, bytes)

def isByteArray(o) -> bool:
    """isByteArray
    Determines if a variable is an bytearray
    Returns:
    bool
    """
    return not isNone(o) and isinstance(o, bytearray)

def isMemoryView(o) -> bool:
    """isMemoryView
    Determines if a variable is an memoryview
    Returns:
    bool
    """
    return not isNone(o) and isinstance(o, memoryview)

def isFunction(f) -> bool:
    """isFunction
    Determines if a variable is an function
    Returns:
    bool
    """    
    return not isNone(f) and callable(f)

def isStringWithLength(o) -> bool:
    """isString
    Determines if a variable is a string with length
    Returns:
    bool
    """    
    return isString(o) and len(o) > 0

def isArray(o) -> bool:
    """isArray
    Determines if a variable is a list, tuple, set or np.ndarray
    Returns:
    bool
    """     
    return not isNone and isinstance(o, (list, tuple, set, np.ndarray))

def isArrayWithLength(o) -> bool:
    """isArrayWithLength
    Determines if a variable is an array with length
    Returns:
    bool
    """      
    return isArray(o) and len(o) > 0

def isTrue(o) -> bool:
    """isTrue
    Determines if a variable is true
    Returns:
    bool
    """      
    return not isNone and o == True

def isFalse(o) -> bool:
    """isFalse
    Determines if a variable is false
    Returns:
    bool
    """      
    return not isTrue(o)

def hasProperty(o: object, prop: str) -> bool:
    """hasProperty
    Determines if an object has property prop
    Returns:
    bool
    """   
    return isObject(o) and hasattr(o, prop)

def getProperty(o: object, prop: str) -> bool:
    """getProperty
    Return an object's property prop
    Returns:
    bool
    """   
    return not isNone(o) and getattr(o, prop)         
    
def init(o: object, prop: str, value = None): 
    """init
    return's an object's property or default variable
    returns any
    """      
    if (hasProperty(o, prop)):
        getProperty(o, prop)
        
    return value 

def isDate(o) -> bool:
    """isDate
    Returns is o is of type date
    Returns:
    bool
    """      
    return not isNone(o) and isinstance(o, datetime.date)

def isTime(o) -> bool:
    """isTime
    Returns is o is of type date
    Returns:
    bool
    """      
    return not isNone(o) and isinstance(o, datetime.time)