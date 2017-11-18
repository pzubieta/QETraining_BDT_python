import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='main.log',
                    filemode='w')

console = logging.StreamHandler()
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def login_msg(logging_type, msg):
    if logging_type == 'debug':
        logging.debug(msg)
    else:
        logging.info(msg)
#tete