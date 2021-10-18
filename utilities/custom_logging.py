import inspect
import logging

def log(loglevel):

    tcname = inspect.stack()[1][3]
    logger = logging.getLogger(tcname)
    logger.setLevel(logging.DEBUG)
    filehandler = logging.FileHandler("automation.log")
    filehandler.setLevel(loglevel)
    format= logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    filehandler.setFormatter(format)
    logger.addHandler(filehandler)
    return logger