import asyncio
import random
from telethon import TelegramClient

api_id = 28923834
api_hash = "31ffb3266550f7a7d8a78c63ffc74e4b"
chat_id = -1002732008495

client = TelegramClient("session", api_id, api_hash)

async def human_pause():
    # استراحت‌های انسانی طولانی‌تر
    if random.random() < 0.15:  # 15% احتمال استراحت طولانی
        long_break = random.randint(600, 1800)  # 10 تا 30 دقیقه
        print(f"Long break: {long_break}s")
        await asyncio.sleep(long_break)

async def main():
    await client.start()

    start_time = asyncio.get_event_loop().time()
    max_runtime = 6 * 60 * 60  # 6 ساعت

    sent_count = 0
    daily_limit = 120  # محدودیت نرم (خیلی مهم برای safety)

    while True:
        # پایان 6 ساعت
        if asyncio.get_event_loop().time() - start_time > max_runtime:
            break

        # محدودیت تعداد پیام
        if sent_count >= daily_limit:
            break

        await client.send_message(chat_id, "میو")
        sent_count += 1

        # استراحت انسانی
        await human_pause()

        # فاصله طبیعی
        wait_time = random.randint(300, 420)
        await asyncio.sleep(wait_time)

with client:
    client.loop.run_until_complete(main())
