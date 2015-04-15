#!/usr/bin/env python
#-*-coding: utf8-*-
__author__ = 'sunzhijie'
import sys
def test():
    args = sys.argv
    if(len(args) == 1):
        return args[0]
    elif(len(args) == 2):
        return 'the file name is' + args[0] + ' and the params is '+ args[1]
    else:
        return 'error'

if __name__ == '__main__':
    print test()

