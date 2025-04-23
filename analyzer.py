import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_channel(data):
    prompt = f"""
Ты — маркетолог-аналитик. Проанализируй Telegram-канал:

📌 Название: {data['title']}
📎 Описание: {data['description']}
📌 Закреп: {data['pinned']}
📝 Последние посты:
{data['posts']}

Дай:
1. Кто ЦА?
2. Есть ли воронка?
3. Что можно усилить?
4. Общую оценку канала.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=800
    )
    return response['choices'][0]['message']['content']