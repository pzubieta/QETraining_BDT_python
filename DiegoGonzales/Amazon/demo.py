import logging
logger = logging.getLogger('myapp')
logger.setLevel(logging.DEBUG)
logger.error('We have a problem')
logger.info('While this is just chatty')