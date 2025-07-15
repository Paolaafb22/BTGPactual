# app/routers/auth.py
from fastapi import APIRouter, HTTPException, status,Depends
from app.schemas.user_schema import UserSignup
from app.core.database import users_collection
from app.core.security import ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi.security import OAuth2PasswordRequestForm

from app.core.security import hash_password,verify_password, create_access_token
from pymongo.errors import DuplicateKeyError
from datetime import timedelta

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
    user_dict["hashed_password"] = hash_password(user.password)
    user_dict["balance"] = 500_000

    users_collection.insert_one(user_dict)

    return {"message": "Usuario registrado exitosamente"}

@auth_router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # form_data.username será el email
    user = users_collection.find_one({"email": form_data.username})
    
    if not user:
        raise HTTPException(status_code=400, detail="Credenciales inválidas")

    if not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Credenciales inválidas")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["email"]},  # También puedes guardar _id o identificacion si prefieres
        expires_delta=access_token_expires
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
