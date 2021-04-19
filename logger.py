import logging


def log(message, access_level):
    logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a',
                            format='%(name)s - %(levelname)s - %(message)s')
    logging.log(access_level, message)
