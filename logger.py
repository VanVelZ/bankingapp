import logging


def log(message, access_level=10):
    logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a',
                        format='%(levelname)s - %(message)s')
    logging.log(access_level, message)
