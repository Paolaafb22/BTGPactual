# app/models/user.py
from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    name: str
    email: EmailStr
    phone: str
    notification_preference: str  # "email" o "sms"
    password: str
    identification:str
    balance: Optional[int] = Field(default=500000)
