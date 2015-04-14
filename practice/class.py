__author__ = 'dazhi'
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print "the name is %s and the score is %s" %(self.name, self.score)

a = Student('lily', 30)
b = Student('Tom', 20)
print a.print_score()
print b.print_score()
a.age = 1
print a.age
b.age