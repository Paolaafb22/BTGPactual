# app/models/user.py
from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    id: Optional[str] = Field(default_factory=str)
    name: str
    email: EmailStr
    phone: str
    notification_preference: str  # "email" o "sms"
    password: str
    identification:str
    balance: float = 500000  # Monto inicial por regla de negocio
    role: str = "cliente"
