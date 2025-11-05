# class Student:
#     def __init__(self, age):
#         self.age = age

#     def print_age(self):
#         print(f'Student age: {self.age}')

# s = Student(21)
# s.age = -100
# s.print_age()

# class Student:
#     def __init__(self, age):
#         self.set_age(age)

#     def set_age(self, age):
#         if age < 0:
#             self._age = 0
#         else:
#             self._age = age

#     def get_age(self):
#         return self._age

#     def print_age(self):
#         print(f'Student age: {self._age}')

# s = Student(20)
# s.print_age()

class Student:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            self._age = 0
        else:
            self._age = age

    def print_age(self):
        print(f'Student age: {self.age}')

s = Student(20)
s.age = -50
print(s.age)