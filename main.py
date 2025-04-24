from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "ok", "message": "API работает"}

@app.post("/analyze")
async def analyze():
    return {"status": "ok", "message": "Запрос получен"}
