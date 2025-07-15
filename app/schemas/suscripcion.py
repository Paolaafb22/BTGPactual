# app/schemas/suscripcion.py

from pydantic import BaseModel

class SuscripcionRequest(BaseModel):
    user_id: str
    fondo_id: str
