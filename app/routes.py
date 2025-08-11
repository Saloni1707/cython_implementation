from fastapi import APIRouter,HTTPException
from datetime import datetime
from app import db
from app.models import MessageSend,MessageReceive
from utils import cy_helpers

router=APIRouter()

@router.post("/messages",response_model=MessageReceive)
async def send_message(payload:MessageSend):
    cleaned=cy_helpers.sanitize_text(payload.content)
    doc={
        "content":cleaned,
        "timestamp":datetime.now(),
    }
    res = await db.messages.insert_one(doc)
    return MessageReceive(id=str(res.inserted_id),content=cleaned,timestamp=doc["timestamp"])


@router.get("/messages")
async def get_messages(limit:int=50):
    docs=await db.messages.find().sort("timestamp",-1).to_list(length=limit)
    results=[{
        "id":str(d.get("_id")),
        "content":d.get("content"),
        "timestamp":d.get("timestamp")
    } for d in docs]
    return results



