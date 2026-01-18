import logging
import os
from datetime import datetime

LOG_File = f"{datetime.now().strftime('%Y-%m-%d')}.log"
logs_Path = os.path.join(os.getcwd(), "logs", LOG_File)
os.makedirs(logs_Path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_Path, LOG_File)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
