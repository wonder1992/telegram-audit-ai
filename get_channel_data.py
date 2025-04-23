async def get_channel_data(client, username):
    chat = await client.search_public_chat(username)
    chat_info = await client.get_chat(chat.id)

    pinned = None
    if chat_info.pinned_message:
        pinned = chat_info.pinned_message.content.text.text

    history = await client.get_chat_history(chat.id, limit=5)
    posts = [m.content.text.text for m in history if m.content and hasattr(m.content, 'text')]

    return {
        "title": chat_info.title,
        "description": chat_info.description,
        "pinned": pinned or "Закреп не найден",
        "posts": posts
    }