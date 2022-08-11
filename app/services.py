import sqlite3

from app import settings


class DBDriver:
    def __init__(self):
        self.__connection = sqlite3.connect(settings.SQLITE3_DATABASE_FILE)
        self.__cursor = self.__connection.cursor()
        self.__first_start()

    def __first_start(self):
        # Создадим таблицу для хранения цитат
        try:
            query = '''
                CREATE TABLE cites
                    (
                        cite text, 
                        show_counter integer
                    )
                '''
            fe = self.__cursor.execute(query)
            print(fe)
            self.__connection.commit()
        except sqlite3.OperationalError:
            print('sqlite3.OperationalError')
            pass

    def new_cite_to_db(self, cite_text: str):
        if not isinstance(cite_text, str):
            print(f'Цитата "{cite_text}" не является текстом, передан тип '
                  f'{type(cite_text)}')
            return False

        query = f"INSERT INTO cites VALUES ('{cite_text}', 0)"
        self.__cursor.execute(query)

        self.__connection.commit()

        return True

    def close_connection(self):
        self.__connection.close()

    @property
    def get_cursor(self):
        return self.__cursor

    @property
    def get_connection(self):
        return self.__connection


if __name__ == '__main__':
    db_driver = DBDriver()

    db_driver.new_cite_to_db(1)
    db_driver.new_cite_to_db('Какой-то текст цитаты 2')

    db_driver.close_connection()
