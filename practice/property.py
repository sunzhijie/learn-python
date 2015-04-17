__author__ = 'sunzhijie'
class Person(object):
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError('the value is not int')
        elif value < 0 or value > 100:
            raise ValueError('the value is not in (1..100)')
        else:
            self.__age = value

p = Person()
p.age = 10
print p.age


