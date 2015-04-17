__author__ = 'sunzhijie'
import os

print os.getenv('PATH')
print os.path.abspath('.')
print os.path.join('/user/', 'dfdf')
# print os.mkdir('./name')
# print os.rmdir('./name')
print [x for x in os.listdir('.') if os.path.splitext(x)[1] == '.py']
