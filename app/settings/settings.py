import logging
import os.path
from pathlib import Path

from dotenv import load_dotenv

# Project source folder
BASE_DIR = Path(__file__).parent.parent.parent

load_dotenv(os.path.join(BASE_DIR, '.env'))

# Setup logging level for logger
LOGGING_LEVEL = logging.DEBUG
LOG_FOLDER = os.path.join(BASE_DIR, r'app/logs')
EVENT_LOG_FILE = os.path.join(LOG_FOLDER, 'event.log')

# Project default encoding
ENCODING = 'utf-8'

SQLITE3_DATABASE_FILE = os.path.join(BASE_DIR, 'sqlite3.db')

CITE_SEND_TIME = os.getenv('CITE_SEND_TIME', default="10:00")
