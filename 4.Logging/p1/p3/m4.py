import logging



'''
logger.setLevel(logging.DEBUG)
format=logging.Formatter('%(message)s')
file_handler=logging.FileHandler('p1.log')
logger.addHandler(file_handler)
stream_handler=logging.StreamHandler()
logger.addHandler(stream_handler)
'''

def f6():
    log4 = logging.getLogger('p1kosam')
    log4.info("entering method f6")
    log4.info("exiting method f6")