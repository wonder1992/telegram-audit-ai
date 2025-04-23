import os
from aiotdlib import create_client

async def start_tdlib():
    client = await create_client(
        api_id=int(os.getenv("TELEGRAM_API_ID")),
        api_hash=os.getenv("TELEGRAM_API_HASH"),
        encryption_key=os.getenv("TDLIB_ENCRYPTION_KEY"),
        library_path="tdjson"
    )
    return client