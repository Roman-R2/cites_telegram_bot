"""Кофнфиг серверного логгера"""
from app.logger.logger import GetLogger

EVENT_LOGGER = GetLogger(logger_name='event_logger').get_logger()

# отладка
if __name__ == '__main__':
    EVENT_LOGGER.critical('Критическая ошибка')
    EVENT_LOGGER.error('Ошибка')
    EVENT_LOGGER.debug('Отладочная информация')
    EVENT_LOGGER.info('Информационное сообщение')
