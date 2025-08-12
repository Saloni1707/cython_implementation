from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

cdef class MongoUtils:
    cdef object client, db

    def __init__(self, str url, str db_name):
        self.client = AsyncIOMotorClient(url)
        self.db = self.client[db_name]

    async def insert_message(self, str collection_name, dict doc):
        try:
            result = await self.db[collection_name].insert_one(doc)
            return str(result.inserted_id)
        except Exception as e:
            raise RuntimeError(f"Failed to insert message: {str(e)}")

    async def get_messages(self, str collection_name):
        try:
            cdef list docs=[]
            cdef object cursor = await self.db[collection_name].find()
            async for doc in cursor:
                if '_id' in doc:
                    doc['_id'] = str(doc['_id'])
                docs.append(doc)
            return docs
        except Exception as e:
            raise RuntimeError(f"Failed to get message: {str(e)}")
            
