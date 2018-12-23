#!/usr/bin/env python3

import logging
from config import Config

class Log():


    @classmethod
    def get_logger(cls):
        try:
            log_path = Config.LOG_APP_PATH
        except Exception as e:
            raise Exception("[Error] app log path not found!")

        logger = logging.getLogger(__name__)
        logger.setLevel(level=logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        if not logger.handlers:
            handler = logging.FileHandler(log_path, encoding='utf-8')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        return logger