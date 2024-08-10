import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)

    filehandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s : %(message)s")
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)
    logger.setLevel(logging.CRITICAL)
    logger.debug("debug statement")
    logger.info("info msg")
    logger.error("error msg")
    logger.critical("critical msg")
    logger.warning("warning msg")






