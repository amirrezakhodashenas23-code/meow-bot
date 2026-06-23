import asyncio
import random
from telethon import TelegramClient

api_id = 28923834
api_hash = "31ffb3266550f7a7d8a78c63ffc74e4b"
chat_id = -1002732008495

client = TelegramClient("session", api_id, api_hash)

async def main():
    # اتصال امن (مناسب GitHub Actions)
    await client.connect()

    # بررسی لاگین بودن
    if not await client.is_user_authorized():
        print("❌ Session not authorized. Run locally once to login.")
        return

    start_time = asyncio.get_event_loop().time()
    max_runtime = 6 * 60 * 60  # 6 hours

    sent_count = 0
    daily_limit = 120

    while True:
        # توقف بعد از 6 ساعت
        if asyncio.get_event_loop().time() - start_time > max_runtime:
            break

        # محدودیت پیام
        if sent_count >= daily_limit:
            break

        try:
            await client.send_message(chat_id, "میو")
            sent_count += 1
            print(f"Sent #{sent_count}")

        except Exception as e:
            print("Send error:", e)
            await asyncio.sleep(15)
            continue

        # استراحت انسانی (مهم برای safe بودن)
        await asyncio.sleep(random.randint(300, 420))

    await client.disconnect()

# اجرای استاندارد (جلوگیری از exit code 139)
if name == "main":
    asyncio.run(main())
