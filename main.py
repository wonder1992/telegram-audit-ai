from fastapi import FastAPI, Request
from td_client import start_tdlib
import os
import openai

app = FastAPI()
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.get("/")
async def root():
    return {"message": "TDLib Telegram Audit API"}

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    channel_url = data.get("channel_url")
    client = await start_tdlib()

    # Временные заглушки — заменим на реальные данные позже
    title = "Пример канала"
    description = "Описание канала"
    pinned = "Закреплённый пост"
    posts = ["Пост 1", "Пост 2", "Пост 3"]

    prompt = f"""
Ты — эксперт по Telegram-маркетингу. Проанализируй Telegram-канал по следующей методологии.

📌 Данные канала:
Название: {title}
Описание: {description}
Закреп: {pinned}
Посты: {posts}

🔍 Методология анализа канала:

1. Пост-закреп: это воронка–навигация “путь клиента” внутри канала с переходами на другие важные посты. Структура: про что канал, кому подойдёт (3 боли), кто автор (переход на пост «обо мне»), оффер, ценность, ссылки, CTA с кнопкой.
2. Пост “Обо мне”: позиционирование, инструменты, кейсы, интересные факты, оффер на воронку.
3. Полезные посты: триггерное название, боль, решение, польза, призыв или вовлечение.
4. Пост с лид–магнитом: боль, что внутри подарка, инструкция как получить, кнопка с ботом.
5. Название канала: имя + ключевое слово (поисковое).
6. Описание: про что канал, зачем подписаться, ссылка на закреп.
7. Контент–стратегия: 14-дневный прогрев по циклу:
   День 1 — вовлечение / боль
   День 2 — почему ты эксперт
   День 3 — ошибки и переход
   День 4 — решение и метод
   День 5 — кейсы клиентов
   День 6 — закрытие возражений
   День 7 — лайф / вдохновение
   День 8 — вовлечение: «устрою эфир — хотите?»
   День 9 — анонс эфира + регистрация
   День 10 — подарки + зачем приходить
   День 11 — день эфира: 4 поста (напоминание, закулисье, начало, призыв)
   День 12 — эмоции и отзывы после эфира
   День 13 — отработка возражений
   День 14 — кейс + призыв на продукт
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Ты эксперт по Telegram-маркетингу."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    analysis_result = response["choices"][0]["message"]["content"]

    return {
        "status": "success",
        "channel_url": channel_url,
        "analysis": analysis_result
    }

# Автозапуск с корректным портом
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
