from fastapi import FastAPI, Request
from td_client import start_tdlib
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "TDLib Telegram Audit API"}

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    channel_url = data.get("channel_url")
    client = await start_tdlib()
    return {"status": "connected", "channel_url": channel_url}