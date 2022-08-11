import os

import telebot
from dotenv import load_dotenv

from app import settings
from app.services import DBDriver


class TelegramBot:
    def __init__(self):
        self.bot = telebot.TeleBot(TELEGRAM_TOKEN)

    def send_message_to_channel(self, message: str):
        self.bot.send_message(CHAT_ID, message)
        self.pooling()

    def pooling(self):
        self.bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    load_dotenv(os.path.join(settings.BASE_DIR, '.env'))

    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    CHAT_ID = os.getenv('CHAT_ID')

    db_driver = DBDriver()

    random_cite = db_driver.get_random_cite()

    cite_string = f""" {random_cite[2]}\n-----------------\n{random_cite[3]}"""

    if cite_string:
        TelegramBot().send_message_to_channel(cite_string)
        print('Цитата отправлена...')
    else:
        print('Логируем ошибку...')
