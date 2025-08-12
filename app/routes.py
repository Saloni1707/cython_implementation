from fastapi import APIRouter,HTTPException
from datetime import datetime
from app.models import MessageSend,MessageReceive
from utils import cy_helpers
from utils.mongo_utils import MongoUtils
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URL=os.getenv("MONGO_URL")
router=APIRouter()
mongo_utils=MongoUtils(MONGO_URL,"messenger_db")

@router.post("/send",response_model=MessageReceive)
async def send_message(payload:MessageSend):
    cleaned=cy_helpers.sanitize_text(payload.content)
    doc={
        "content":cleaned,
        "timestamp":datetime.now(),
    }
    inserted_id = await mongo_utils.insert_message("messages",doc)
    return MessageReceive(id=inserted_id,content=cleaned,timestamp=doc["timestamp"])


@router.get("/receive",response_model=list[MessageReceive])
async def get_messages():
    docs=await mongo_utils.get_messages("messages")
    results=[{
        "id":str(d.get("_id")),
        "content":d.get("content"),
        "timestamp":d.get("timestamp")
    } for d in docs]
    return results



