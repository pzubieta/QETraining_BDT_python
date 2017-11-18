import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create a file handler
hadler = logging.FileHandler ('test_log.log')

# Create a logging format
formatter = logging.Formatter ('%(asctime)s - %(name)s - %(levelname)s - % (message)s')
hadler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(hadler)

logger.info('Start reading database')
# read database here
records = {'john': 55, 'tom':66}
logger.debug('Records: %s', records)
logger.info('Updating records... ')
# update records here
logger.info ('Finished updating records')