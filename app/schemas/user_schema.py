# app/schemas/user_schema.py
from pydantic import BaseModel, EmailStr, Field

class UserSignup(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(min_length=6)
    phone: str
    notification_preference: str  # "email" o "sms"
    identification: str = Field(..., min_length=10, max_length=20)
