import logging
from datetime import datetime
import os
from time import strftime

LOG_DIR="logs"
CURRENT_TIME_STAMP = f"{datetime.now(),strftime('%Y-%m-%d_%H-%M-%S')}"

#def get_log_file_name():
#    return f"log_{get_current_time_stamp()}.log"

LOG_FILE_NAME=f"log_{CURRENT_TIME_STAMP}.log"

os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)



logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s]^;%(levelname)s^;%(lineno)d^;%(filename)s^;%(funcName)s()^;%(message)s',
level=logging.INFO
)