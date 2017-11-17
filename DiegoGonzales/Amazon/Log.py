import logging

class Log:

    def __init__(self, type=""):
        self.log_ = logging.getLogger('Amazon')
        self.file_ = logging.FileHandler('Amazon.log')
        self.formatter = logging.Formatter('%(asctime)s _ %(levelname)s _ %(message)s')
        self.file_.setFormatter(self.formatter)
        self.log_.addHandler(self.file_)

    def log_error(self, message):
        self.log_.error(message)

    def log_info(self, message):
        self.log_.info(message)

    def log_warning(self, message):
        self.log_.warning(message)

    def log_critical(self, message):
        self.log_.critical(message)

    def log_debug(self, message):
        self.log_debug(message)

log = Log()
log.log_error("Putin eres un logo")
log.log_critical("Error desistema")
log.log_warning("Tu sistema necesita installar porn")