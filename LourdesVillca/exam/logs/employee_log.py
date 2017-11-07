import logging

logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger(__name__)
handler = logging.FileHandler('application.log')

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(lineno)d - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
LOG.addHandler(handler)
