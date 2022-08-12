import os
import sqlite3
import datetime

from dotenv import load_dotenv

from app import settings


class DBDriver:
    def __init__(self):
        self.__id_field = 'id'
        self.__cite_table_name = 'cites'
        self.__cite_text_field = 'cite'
        self.__counter_field = 'show_counter'
        self.__owner_field = 'owner'

        self.__connection = sqlite3.connect(settings.SQLITE3_DATABASE_FILE)
        self.__cursor = self.__connection.cursor()

    def __first_start(self):
        # Создадим таблицу для хранения цитат
        try:
            query = f'''
                CREATE TABLE {self.__cite_table_name}
                    (
                        {self.__id_field} INTEGER PRIMARY KEY,
                        {self.__cite_text_field} TEXT,
                        {self.__owner_field} TEXT,
                        {self.__counter_field} INTEGER
                    )
                '''
            self.__cursor.execute(query)
            self.__connection.commit()
        except sqlite3.OperationalError:
            print('sqlite3.OperationalError')
            ErrorLogger.write_error('sqlite3.OperationalError. Ошибка базы '
                                    'данных.')

    def new_cite_to_db(self, cite_text: str, cite_owner: str):
        if not isinstance(cite_text, str):
            print(f'Цитата "{cite_text}" не является текстом, передан тип '
                  f'{type(cite_text)}')
            return False

        query = f"INSERT INTO {self.__cite_table_name} (" \
                f"{self.__cite_text_field}, {self.__counter_field}, " \
                f"{self.__owner_field}) VALUES ('{cite_text}', 0, '{cite_owner}')"
        try:
            self.__cursor.execute(query)
        except:
            print('Пытаемся создать таблицу...')
            self.__first_start()
            self.__cursor.execute(query)

        self.__connection.commit()

        return True

    def close_connection(self):
        self.__connection.close()

    def get_random_cite(self):
        """ Вернет случайную цитату из БД и увеличит поле показа цитаты
        на 1 """
        query = f"SELECT {self.__id_field}" \
                f", {self.__counter_field}" \
                f", {self.__cite_text_field}" \
                f", {self.__owner_field} " \
                f"FROM" \
                f" {self.__cite_table_name} " \
                f"WHERE {self.__counter_field} = (" \
                f"  SELECT MIN({self.__counter_field}) " \
                f"  FROM {self.__cite_table_name})" \
                f"ORDER BY RANDOM() " \
                f"LIMIT 1 "
        query_result = self.__cursor.execute(query).fetchone()

        # print(f'{query_result=}')

        this_field_id = query_result[0]
        this_field_counter = int(query_result[1])

        increment_query = f"""
            UPDATE {self.__cite_table_name}
            SET {self.__counter_field} = {this_field_counter + 1}
            WHERE {self.__id_field} = {this_field_id}
        """

        self.__cursor.execute(increment_query)
        self.__connection.commit()

        return query_result

    @property
    def get_cursor(self):
        return self.__cursor

    @property
    def get_connection(self):
        return self.__connection


class ErrorLogger:

    def __init__(self):
        load_dotenv(os.path.join(settings.BASE_DIR, '.env'))
        self.error_file = os.path.join(
            settings.BASE_DIR,
            os.getenv('TXT_FILE_FOR_ERRORS')
        )

    def write_error(self, error_text: str):
        with open(self.error_file, mode='a', encoding='utf-8') as fd:
            fd.write(str(datetime.datetime.now()) + ' ' + error_text + '\n')


if __name__ == '__main__':
    print("Это сервисный файл, из него нужно подключить классы")
    DBDriver().get_random_cite()
