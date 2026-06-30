pythonimport asyncio
from telethon import TelegramClient

# --- 請把下方的 12345 和 '你的api_hash' 換成第一步拿到的鑰匙 ---
api_id = 35938210
api_hash = '03a1cb6569098d4bac300c76cd53af5f'
# -------------------------------------------------------------

async def main():
    async with TelegramClient('online_session', api_id, api_hash) as client:
        print("連線成功！正在幫您維持在線上...")
        while True:
            # 每 4 分鐘偷偷讀取一次自己的資訊，讓伺服器知道你還在
            await client.get_me()
            await asyncio.sleep(240)

if __name__ == '__main__':
    asyncio.run(main())
