# app/models/fondo.py

from pydantic import BaseModel
from typing import Optional

class Fondo(BaseModel):
    id: str
    nombre: str
    monto_minimo: float
    categoria: str
