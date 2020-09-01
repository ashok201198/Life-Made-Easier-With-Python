import logging

'''
logger.setLevel(logging.DEBUG)
format=logging.Formatter('%(message)s')
file_handler=logging.FileHandler('p2.log')
logger.addHandler(file_handler)
stream_handler=logging.StreamHandler()
logger.addHandler(stream_handler)
'''

def f3():
    log1 = logging.getLogger('p2kosam')
    log1.info("entering method f3")
    log1.info("exiting method f3")

def f4():
    log1 = logging.getLogger('p2kosam')
    log1.info("entering method f4")
    log1.info("exiting method f4")