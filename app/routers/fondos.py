# routes/fondos.py

from fastapi import APIRouter, Depends
from schemas.suscripcion import SuscripcionRequest
from services.fondos import suscribirse_a_fondo
from app.core.database import get_db

from auth import get_current_user  # si usas autenticación con JWT


router = APIRouter()

@router.post("/suscribirse")
def suscribirse(data: SuscripcionRequest, db=Depends(get_db), current_user=Depends(get_current_user)):
    return suscribirse_a_fondo(db, current_user["id"], data.fondo_id)

