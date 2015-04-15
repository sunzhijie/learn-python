__author__ = 'sunzhijie'
a = [1, 2, 3, 4, 5, 6]
def is_odd(x):
    if(x % 2 == 0):
        return True
    else:
        return False

print filter(is_odd, a)
