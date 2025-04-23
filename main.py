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

# Автозапуск с корректным портом
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
