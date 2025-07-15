# app/core/database.py

from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)

db = client["fondos_btg"]  # Nombre de la base de datos
users_collection = db["users"]
funds_collection = db["funds"]
transactions_collection = db["transactions"]

def get_db():
    return db
