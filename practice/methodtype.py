__author__ = 'sunzhijie'
from types import MethodType


class Person(object):
    __slots__ = ('name', 'age', 'get_name')


per = Person()
per.name = 'name'
print per.name


def get_name(self, text):
    return self.name + text


per.get_name = MethodType(get_name, per, Person)
print per.get_name('hello')

Person.get_name = MethodType(get_name, None, Person)
per1 = Person()
per1.name = 'a'
print per1.get_name('fd')

# slots
# per.sex = 'man'
# print per.sex


class Lily(Person):
    pass


li = Lily()
li.sex = 'female'
print li.sex
