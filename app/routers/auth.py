# app/routers/auth.py
from fastapi import APIRouter, HTTPException, status
from app.schemas.user_schema import UserSignup
from app.core.database import users_collection
from app.core.security import hash_password
from pymongo.errors import DuplicateKeyError

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/signup")
def signup(user: UserSignup):
    existing = users_collection.find_one({"email": user.email})
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El correo ya está registrado"
        )
    
    user_dict = user.dict()
    user_dict["password"] = hash_password(user.password)
    user_dict["balance"] = 500_000

    users_collection.insert_one(user_dict)

    return {"message": "Usuario registrado exitosamente"}
