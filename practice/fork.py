__author__ = 'sunzhijie'
import os

print "process (%s) start..." % os.getpid()
pid = os.fork()
if pid == 0:
    print 'i am child process (%s), my parent is (%s)' %(os.getpid(), os.getppid())
else:
    print 'i (%s) create a child process (%s)' %(os.getpid(), pid)
