import logging
from ast import literal_eval


def make_it_literal(x):
    try:
        return literal_eval(x)
    except:
        return x


def get_logger(name, log_level=logging.INFO):
    logging.basicConfig(level=log_level)
    logger = logging.getLogger(name)
    return logger
