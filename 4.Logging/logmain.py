import logging
from logging.config import dictConfig
from p1 import m1,m3
from p1.p2 import m2
from p1.p3 import m4

logging_config = dict(
    version = 1,
    #disable_existing_loggers=True,
    formatters = {
        'f': {'format':
              '%(message)s'}
        },
    handlers = {
        's': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logging.WARNING,
              },
        'f': {'class': 'logging.FileHandler',
              'formatter': 'f',
              'level': logging.DEBUG,
              'filename':'main.log'
              },
        'f1': {'class': 'logging.FileHandler',
              'formatter': 'f',
              'level': logging.DEBUG,
              'filename':'p1.log'
              },
        'f2': {'class': 'logging.FileHandler',
              'formatter': 'f',
              'level': logging.DEBUG,
              'filename':'p2.log'
              }
        },
    loggers={
    'main' : {
            'handlers': ['s','f'],
            'level': logging.DEBUG,
            },
    'p1kosam' : {
            'handlers': ['s','f1'],
            'level': logging.DEBUG,
            },
    'p2kosam' : {
            'handlers': ['s','f2'],
            'level': logging.DEBUG,
            },
    }
)

logging.config.dictConfig(logging_config)

'''
logger.setLevel(logging.DEBUG)
format=logging.Formatter('%(message)s')
file_handler=logging.FileHandler('main.log')
logger.addHandler(file_handler)
stream_handler=logging.StreamHandler()
logger.addHandler(stream_handler)
'''
logger=logging.getLogger('main')
#logger.disabled=True
m1.f1()
m1.f2()
m2.f3()
m2.f4()
m3.f5()
m4.f6()

#logger.disabled=False
logger.info("this is from main")
