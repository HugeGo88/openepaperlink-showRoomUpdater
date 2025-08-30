import logging


def setup_logging(log_file='app.log'):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # File handler
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)
    fh_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(fh_formatter)

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch_formatter = logging.Formatter('%(levelname)s - %(message)s')
    ch.setFormatter(ch_formatter)

    # Avoid duplicate handlers
    if not logger.hasHandlers():
        logger.addHandler(fh)
        logger.addHandler(ch)
    else:
        logger.handlers.clear()
        logger.addHandler(fh)
        logger.addHandler(ch)
