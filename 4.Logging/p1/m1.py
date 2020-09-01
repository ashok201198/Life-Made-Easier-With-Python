import logging

'''
logger.setLevel(logging.DEBUG)
format=logging.Formatter('%(message)s')
file_handler=logging.FileHandler('p1.log')
logger.addHandler(file_handler)
stream_handler=logging.StreamHandler()
logger.addHandler(stream_handler)
'''

def f1():
    log2 = logging.getLogger('p1kosam')
    log2.info("entering method f1")
    log2.info("exiting method f1")
    log2.warning("this is a log of warning from f1")

def f2():
    log2 = logging.getLogger('p1kosam')
    log2.info("entering method f2")
    log2.info("exiting method f2")