# Here we put FastAPI models
from typing import List, Optional
from pydantic import BaseModel


class CustomerInfo(BaseModel):
    id: str
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    sex: Optional[str] = None
    address: Optional[str] = None
    birthDate: Optional[str] = None
    phoneMobile: Optional[str] = None
    phoneHome: Optional[str] = None
    phoneBusiness: Optional[str] = None
    emailHome: Optional[str] = None
    emailBusiness: Optional[str] = None
    company: Optional[str] = None




