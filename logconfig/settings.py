import os
import logging.config
import json

class LoggingSettings:
    DEFAULT_LOGGING_CONFIG_PATH = 'logconfig/config/logging.json'
    SYSTEM_LOGGING_CONFIG_VARIABLE = 'LOG_CFG'

    def __init__(self):
        self.default_path = self.DEFAULT_LOGGING_CONFIG_PATH
        self.default_level = logging.INFO
        self.env_key = self.SYSTEM_LOGGING_CONFIG_VARIABLE

    def configure(self):
        """Setup logging configuration
        """
        path = self.default_path
        value = os.getenv(self.env_key, None)
        if value:
            path = value
        if os.path.exists(path):
            with open(path, 'rt') as f:
                config = json.load(f)
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=self.default_level)
