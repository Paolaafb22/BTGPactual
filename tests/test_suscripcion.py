# tests/test_suscripcion.py

import pytest
import mongomock
from datetime import datetime
from uuid import uuid4

from app.services.fondos import suscribirse_a_fondo


@pytest.fixture
def fake_db():
    client = mongomock.MongoClient()
    db = client["fondos_btg"]
    return db


def test_suscripcion_exitosa(fake_db):
    # Crear usuario y fondo
    user_id = "user1"
    fondo_id = "fondo1"

    fake_db.users.insert_one({
        "id": user_id,
        "balance": 500000,
        "email": "test@correo.com",
        "name": "Usuario Test"
    })

    fake_db.fondos.insert_one({
        "id": fondo_id,
        "nombre": "FPV_BTG_PACTUAL_ECOPETROL",
        "monto_minimo": 125000,
        "categoria": "FPV"
    })

    # Ejecutar función
    suscribirse_a_fondo(fake_db, user_id, fondo_id)

    user = fake_db.users.find_one({"id": user_id})
    assert user["balance"] == 375000

    transacciones = list(fake_db.transacciones.find({"user_id": user_id}))
    assert len(transacciones) == 1
    assert transacciones[0]["tipo"] == "suscripcion"


def test_fondo_no_existe(fake_db):
    user_id = "user2"
    fake_db.users.insert_one({"id": user_id, "balance": 500000})

    with pytest.raises(Exception) as e:
        suscribirse_a_fondo(fake_db, user_id, "fondo_inexistente")
    assert "Usuario o fondo no encontrado" in str(e.value)


def test_saldo_insuficiente(fake_db):
    user_id = "user3"
    fondo_id = "fondo3"

    fake_db.users.insert_one({"id": user_id, "balance": 30000})
    fake_db.fondos.insert_one({
        "id": fondo_id,
        "nombre": "FDO-ACCIONES",
        "monto_minimo": 250000,
        "categoria": "FIC"
    })

    with pytest.raises(Exception) as e:
        suscribirse_a_fondo(fake_db, user_id, fondo_id)
    assert "No tiene saldo disponible" in str(e.value)
