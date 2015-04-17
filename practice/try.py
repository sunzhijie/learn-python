__author__ = 'sunzhijie'
try:
    print 'try.....'
    r = 10 / 0
    print 'try result....'
except StandardError, e:
    print 'base except:', e
except ZeroDivisionError, e:
    print 'except:', e
else:
    print 'no error ....'
finally:
    print 'finally'
