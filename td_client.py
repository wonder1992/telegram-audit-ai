from aiotdlib import TDLibClient
import os

client = TDLibClient(
    api_id=int(os.getenv("TELEGRAM_API_ID")),
    api_hash=os.getenv("TELEGRAM_API_HASH"),
    database_encryption_key=os.getenv("TDLIB_ENCRYPTION_KEY")
)

async def start_tdlib():
    await client.start()
    return client