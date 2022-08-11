import os.path

from app import settings
from app.services import DBDriver

counter = 1

db_driver = DBDriver()

with open(
        os.path.join(settings.BASE_DIR, r'data\data_2.txt'),
        mode='r',
        encoding='utf-8'
) as fd:
    start = 1
    end = 300
    text_data = fd.read()

    for num in range(start, end + 1):

        this_delimiter = f'{num}.'
        next_delimiter = f'{num + 1}.'

        # print(f'{this_delimiter=}, {next_delimiter=}')

        start_index = text_data.index(this_delimiter)
        if num == end:
            end_index = -1
        else:
            end_index = text_data.index(next_delimiter)

        db_driver.new_cite_to_db(text_data[start_index + len(
            this_delimiter): end_index], 'Бальтасар Грасиан')
        # print(text_data[start_index + len(this_delimiter): end_index])
        print(counter)
        counter += 1
