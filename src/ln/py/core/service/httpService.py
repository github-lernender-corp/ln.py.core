import asyncio;
from library import (guid)
from model import (Response)


async def fetch(url: str)-> Response:
    """fetch
    Makkes Https Request
    Returns:
    Response object
    """    
    await asyncio.sleep(2.5)
    return Response()