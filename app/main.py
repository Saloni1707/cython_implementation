from fastapi import FastAPI
from app.routes import router as routes
from utils import cy_helpers

app=FastAPI()
app.include_router(routes)

@app.get("/")
def root():
    return {"message":"Anonymous messenger is running"}

@app.get("/health")
def health():
    return {"status":"ok","sanity":cy_helpers.quick_check()}