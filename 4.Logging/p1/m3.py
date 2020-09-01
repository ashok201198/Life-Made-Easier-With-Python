import logging

'''
logger.setLevel(logging.DEBUG)
format=logging.Formatter('%(message)s')
file_handler=logging.FileHandler('p1.log')
logger.addHandler(file_handler)
stream_handler=logging.StreamHandler()
logger.addHandler(stream_handler)
'''
#log3=logging.getLogger('4')

def f5():
    log3 = logging.getLogger('p1kosam')
    log3.info("entering method f5")
    log3.info("exiting method f5")