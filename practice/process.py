__author__ = 'sunzhijie'
from multiprocessing import Process
import os

def run_process(name):
    print 'the child process %s is running, name is %s' %(os.getpid(), name)

if __name__ == '__main__':
    print 'Parent process is %s' %(os.getpid())
    p = Process(target=run_process, args=('test',))
    print 'Child process start ..'
    p.start()
    p.join()
    print 'end'
