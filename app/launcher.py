import datetime

import schedule
import time

from app.main import InitBot

if __name__ == '__main__':

    def job():
        InitBot.start()


    # schedule.every().minute.do(InitBot.start())
    # schedule.every(1).days.do(job)
    schedule.every().day.at("10:00").do(job)

    print(f'Запустили задачу {schedule.jobs}')

    while True:
        schedule.run_pending()
        print(datetime.datetime.now(), schedule.jobs)
        time.sleep(1)
