__author__ = 'sunzhijie'
import logging
logging.basicConfig(level=logging.INFO)
try:
    print 'try.....'
    logging.info('000000')
    r = 10 / 0
    print 'try result....'
except StandardError, e:
    logging.exception(e)
except ZeroDivisionError, e:
    print 'except:', e
else:
    print 'no error ....'
finally:
    print 'finally'

print 'End'

