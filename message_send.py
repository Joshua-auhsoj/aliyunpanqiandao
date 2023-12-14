import requests
import json
from telegram import Bot
import asyncio
import os


class MessageSend:
    def __init__(self):
        self.sender = {}

    def tgbot(self, title, content):
        bot_token = os.environ.get('BOTTOKEN')
        chat_id = os.environ.get('USERID')
        print(title + '\n' + content)

        bot = Bot(token=bot_token)

        # 发送消息
        async def send_message():
            await bot.send_message(chat_id=chat_id, text=title + '\n' + content)

            # 运行异步函数

        asyncio.run(send_message())
