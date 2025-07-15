from fastapi import HTTPException
from datetime import datetime
import uuid

def suscribirse_a_fondo(db, user_id: str, fondo_id: str):
    user = db.users.find_one({"id": user_id})
    fondo = db.fondos.find_one({"id": fondo_id})

    if not user or not fondo:
        raise HTTPException(status_code=404, detail="Usuario o fondo no encontrado")

    if user["balance"] < fondo["monto_minimo"]:
        raise HTTPException(
            status_code=400,
            detail=f"No tiene saldo disponible para vincularse al fondo {fondo['nombre']}"
        )

    # Descontar saldo
    db.users.update_one({"id": user_id}, {"$inc": {"balance": -fondo["monto_minimo"]}})

    # Guardar transacción
    db.transacciones.insert_one({
        "id_transaccion": str(uuid.uuid4()),
        "user_id": user_id,
        "fondo_id": fondo_id,
        "tipo": "suscripcion",
        "monto": fondo["monto_minimo"],
        "fecha": datetime.utcnow()
    })
