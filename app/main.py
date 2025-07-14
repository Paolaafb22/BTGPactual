# app/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API BTG Pactual Fondos aqui vamos"}
