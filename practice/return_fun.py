__author__ = 'sunzhijie'
def lazy_sum(*args):
    def myself():
        ax = 0
        for n in args:
            ax += n
        return ax
    return myself

a = []
f = lazy_sum(1, 2, 3, 4)
# print f()

def my_count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1, f2, f3 = my_count()
print f1()
print f2()
print f3()