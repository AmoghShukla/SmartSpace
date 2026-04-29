import logging
import os


def get_logger(name : str):

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        if not os.path.exists('src/logs'):
            os.mkdir('src/logs')
        
        formatter = logging.Formatter(' %(asctime)s | %(levelname)s | %(name)s | %(message)s ')

        ConsoleHandler = logging.StreamHandler()
        ConsoleHandler.setFormatter(formatter)

        FileHandler = logging.FileHandler('src/logs/app.log')
        FileHandler.setFormatter(formatter)
    
    return logger