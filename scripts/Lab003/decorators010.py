class AgeDescriptor:
    def __get__(self, instance, owner):
        return instance._age

    def __set__(self, instance, value):
        if value < 0:
            instance._age = 0
        else:
            instance._age = value

class Student:
    age = AgeDescriptor()

    def __init__(self, age):
        self.age = age

    def print_age(self):
        print(f'Student age: {self.age}')

s = Student(25)
s.age = -30
print(s.age)