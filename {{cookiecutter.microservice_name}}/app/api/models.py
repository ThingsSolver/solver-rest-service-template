# Here we put FastAPI models
from typing import List, Optional
from pydantic import BaseModel


class Example(BaseModel):
    id: str
    firstName: Optional[str] = None
    lastName: Optional[str] = None




