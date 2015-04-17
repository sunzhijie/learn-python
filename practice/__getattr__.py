__author__ = 'sunzhijie'


class Chain(object):
    def __init__(self, path=''):
        self.__path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.__path, path))

    def __str__(self):
        return self.__path


print Chain().users.name