__author__ = 'sunzhijie'
from multiprocessing import Pool
import os, time, random


def long_task(name):
    print 'running task %s, name is %s' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'task %s runs %0.2f second' % (os.getpid(), (end - start))


if __name__ == '__main__':
    print 'Parent process is (%s)' % (os.getpid())
    p = Pool()
    for i in range(5):
        p.apply_async(long_task, args=(i,))
    p.close()
    p.join()
print 'end'
