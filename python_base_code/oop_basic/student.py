#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    # 特殊方法“__init__”前后分别有两个下划线！！！
    # 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，
    # 就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

print('bart.name =', bart.name)
print('bart.score =', bart.score)
bart.print_score()

print('grade of Bart:', bart.get_grade())
print('grade of Lisa:', lisa.get_grade())
