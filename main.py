from fastapi import FastAPI, Request
import asyncio
from td_client import start_tdlib
from get_channel_data import get_channel_data
from analyzer import analyze_channel

app = FastAPI()
client = None

@app.on_event("startup")
async def startup():
    global client
    client = await start_tdlib()

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    channel_url = data.get("channel_url")
    username = channel_url.replace("https://t.me/", "").strip()

    channel_data = await get_channel_data(client, username)
    analysis = analyze_channel(channel_data)

    return {"result": analysis}