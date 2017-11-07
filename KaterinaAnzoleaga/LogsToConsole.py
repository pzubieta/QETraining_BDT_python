import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info('Start reading database')
# read the db here
record = {'john':55, 'tom':66}
logger.debug('Record: %s', record)
logger.info('Updating records ...')
# update recors here
logger.info('Finishing updating records')