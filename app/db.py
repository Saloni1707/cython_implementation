import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import asyncio

load_dotenv()

MONGO_URL=os.getenv("MONGO_URL")
client=AsyncIOMotorClient(MONGO_URL)
db=client["messenger_db"]
messages=db["messages"]
