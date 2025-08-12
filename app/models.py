from pydantic import BaseModel,Field
from datetime import datetime

class MessageSend(BaseModel):
    content:str=Field(...,max_length=2000)

class MessageReceive(BaseModel):
    id:str
    content:str
    timestamp:datetime