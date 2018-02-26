import logging

def foo():
    logger = logging.getLogger(__name__)
    logger.info('Hi, foo')

class TModule:
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

    def bar(self):
        self.logger.info('Hi, bar')


