# db.py
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

def connect_to_db():
    mongo_pass = os.getenv("MONGO_PASS")
    client = MongoClient(f"mongodb+srv://Liberty:{mongo_pass}@cluster0.ft3kewv.mongodb.net/")
    return client["DBLeisureCentre"]


 
 
 
 
 
 
 
 

