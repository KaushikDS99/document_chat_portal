import os
import logging
from datetime import datetime


##Implementing a custom logger class that can be used accross the project
class CustomLogger:
    def __init__(self):
        self.log_directory = os.path.join(os.getcwd(), "logs")
        os.makedirs(self.log_directory, exist_ok=True)
        self.log_file_name = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
        self.log_file_path = os.path.join(self.log_directory, self.log_file_name)
        logging.basicConfig(filename= self.log_file_path,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            level=logging.INFO)

    def get_logger(self, name= __file__):
        return logging.getLogger(os.path.basename(name))
    

if __name__== "__main__":
    print("Testing the Custom Logger")
    logger = CustomLogger()
    logger = logger.get_logger(__file__)
    logger.info("Custom Logger is initialized.")
    print("Done Testing")