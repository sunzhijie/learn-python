__author__ = 'sunzhijie'
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **ks):
        print 'calling %s..:' + func.__name__
        a = func(*args, **ks)
        print 'end'
        return a
    return wrapper

@log
def now():
    print '2015'

now()
print now.__name__