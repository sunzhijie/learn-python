__author__ = 'sunzhijie'
try:
    import cPickle as pickle
except ImportError, e:
    import pickle

d = dict(name = 'lily', age = 10)
a = pickle.dumps(d)
print '\n'
print pickle.loads(a)
