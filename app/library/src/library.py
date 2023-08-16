"""library
This module is designed to encapsulate common functionality used
by developers into a common library.
"""
import uuid

def guid() -> str:
    """create_guid
    This function creates a standard guid
    Returns:
        str: Guid
    """
    _guid = str(uuid.uuid4())
    _guid = _guid.upper()
    return _guid
    