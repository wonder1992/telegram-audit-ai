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
