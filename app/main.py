from fastapi import FastAPI
from app.routers import auth
from app.routers.auth import auth_router



app = FastAPI()
app.include_router(auth.auth_router)

@app.get("/")
def root():
    return {"message": "API BTG Pactual en ejecución"}
