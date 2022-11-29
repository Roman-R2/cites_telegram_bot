import os

import telebot
from dotenv import load_dotenv

from app.logger.logger import GetLogger
from app.services import DBDriver
from app.settings import settings

EVENT_LOGGER = GetLogger(logger_name='event_logger').get_logger()


class TelegramBot:
    def __init__(self, telegram_token, chat_id):
        self.chat_id = chat_id
        self.bot = telebot.TeleBot(telegram_token, threaded=False)
        print(self.chat_id, self.bot)

    def send_message_to_channel(self, message: str):
        self.bot.send_message(self.chat_id, message)
        # self.bot.polling()


class InitBot:

    def __init__(self):
        load_dotenv(os.path.join(settings.BASE_DIR, '.env'))

        self.telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.chat_id = os.getenv('TELEGRAM_CHANNEL_ID')
        self.db_driver = DBDriver()

    def __start(self):
        random_cite = self.db_driver.get_random_cite()
        cite_string = f""" {random_cite[2]}\n-----------------\n{random_cite[3]}"""

        if cite_string:
            TelegramBot(
                self.telegram_token,
                self.chat_id
            ).send_message_to_channel(
                cite_string
            )
            EVENT_LOGGER.error(
                'Цитата отправлена...'
            )
        else:
            EVENT_LOGGER.error(
                'Ошибка получения цитаты.'
            )

    @staticmethod
    def start():
        return InitBot().__start()


if __name__ == '__main__':
    print(f'Это модуль {__name__}')
