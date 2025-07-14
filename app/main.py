from fastapi import FastAPI
from app.routers import auth

app = FastAPI()
app.include_router(auth.auth_router)

@app.get("/")
def root():
    return {"message": "API BTG Pactual en ejecución"}
