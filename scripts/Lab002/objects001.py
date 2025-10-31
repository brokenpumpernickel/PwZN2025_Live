# pass

# def function():
#     pass

# function()

# class Student:
#     pass

# s1 = Student()
# print(type(s1))

# class Student:
#     classes = []

#     def __init__(self):
#         print('Init student')

# s1 = Student()
# s1.classes.append('PwZN')
# s1.classes.append('FK')
# s1.classes.append('TI')
# s1.classes.append('AM')

# print(s1.classes)

# s2 = Student()
# print(s2.classes)

# print(Student.__dict__)
# print(s1.__dict__)

# class Student:
#     def __init__(self):
#         self.classes = []
#         print('Init student')

# s1 = Student()
# s1.classes.append('PwZN')
# s1.classes.append('FK')
# s1.classes.append('TI')
# s1.classes.append('AM')
# print(s1.classes)

# s2 = Student()
# print(s2.classes)

# s1.age = 20
# print(s1.age)

# print(Student.__dict__)
# print(s1.__dict__)

# class Student:
#     def __init__(self, name, age):
#         self.classes = []
#         self.name = name
#         self.age = age
#         print('Init student')

# s1 = Student('Bożydar', 21)

# s2 = Student('Augustyn', 41)

# print(s1)
# print(s1.name)
# print(s1.age)

# print(Student.__dict__)
# print(s1.__dict__)

# class Student:
#     def __init__(self, name, age):
#         self.classes = []
#         self.name = name
#         self.age = age
#         print('Init student')

#     def print_info(self):
#         print(f'Student name: {self.name}, age: {self.age}, classes: {self.classes}')

# s1 = Student('Bożydar', 21)
# s2 = Student('Augustyn', 41)

# s1.print_info()

# # Student.print_info(s1)
# # Student.__dict__['print_info'](s1)

# print(Student.__dict__)
# print(s1.__dict__)

class Student:
    def __init__(self, name, age):
        self.classes = []
        self.name = name
        self.age = age
        print('Init student')

    def print_info(self):
        print(f'Student name: {self.name}, age: {self.age}, classes: {self.classes}')

    def __str__(self):
        return f'Student name: {self.name}, age: {self.age}, classes: {self.classes}'
    
    def __getitem__(self, index):
        return self.classes[index]

s1 = Student('Bożydar', 21)
s1.classes.append('PwZN')
s1.classes.append('FK')
s1.classes.append('TI')
s1.classes.append('AM')
s1.print_info()

print(s1)

print(s1[0])