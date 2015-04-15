__author__ = 'sunzhijie'
def build(x, y):
    return lambda: x+y
f = build(2, 3)
print f()