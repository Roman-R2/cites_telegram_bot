import datetime
import locale
import time

import schedule

from app.main import InitBot
from app.settings import settings

if __name__ == '__main__':

    # locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

    def job():
        InitBot.start()

    # schedule.every().minute.do(job)
    # schedule.every(1).days.do(job)
    schedule.every().day.at(settings.CITE_SEND_TIME).do(job)

    print(f'Запустили задачу {schedule.jobs}')

    while True:
        schedule.run_pending()
        print(datetime.datetime.now(), schedule.jobs)
        time.sleep(1)
