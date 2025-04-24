from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Сервер работает!"}

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    channel_url = data.get("channel_url")
    
    print(f"📥 Получен канал: {channel_url}")
    
    return {
        "status": "ok",
        "channel_url": channel_url,
        "message": "Сервер работает! Ошибка была в обработке данных."
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
