import logging
import os
from datetime import datetime 

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("Logging has started") #Example to check if logging is happening or not

     
# # src/logger.py
# import logging
# import os
# from datetime import datetime

# # Directory to hold logs
# LOG_DIR = os.path.join(os.getcwd(), "logs")
# os.makedirs(LOG_DIR, exist_ok=True)

# # Timestamped logfile name
# LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
# LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# # Create logger
# logging.basicConfig(
#     level=logging.INFO,
#     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     handlers=[
#         logging.FileHandler(LOG_FILE_PATH, encoding="utf-8"),
#         logging.StreamHandler(),  # prints to console
#     ],
# )

# # Optionally export a module-level logger instance if you prefer:
# logger = logging.getLogger(__name__)

