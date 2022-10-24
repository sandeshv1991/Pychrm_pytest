import logging


class LogGen:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename=".\\Logs\\automation.log", format=r"%(asctime)s: %(levelname)s: %(message)s", datefmt=r"%m/%d/%Y %I:%m: %s %p")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
