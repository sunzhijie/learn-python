__author__ = 'sunzhijie'
import re

a = re.match(r'^(\d{3})\s', '323 dsd ')
print re.split(r'\s+|\,', 'fd,hghg fdf sfs')

print a.groups()
print a.group(0)
print a.group(1)