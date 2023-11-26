import logging
logging.basicConfig(level = logging.INFO, format = ' %(asctime)s, %(process)d - %(name)s - %(levelname)s - %(message)s', datefmt = '%d-%b-%y %H-%M-%S')
a, b = 5,0
try:
    c = a/b

except:
    logging.exception('Exception Occured', exc_info = True)
logging.debug('This is a debug message')
logging.info('Ths is user trying to steal')
logging.warning('Admin logged out')
logging.error('This is an error message')
logging.critical('This is a critical message')
