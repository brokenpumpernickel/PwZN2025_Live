# def function(x, y, z=10):
#     print(f'x: {x}, y: {y}, z: {z}')

# function(1, 2, z=3)

# def function(x, y, *args, z=10):
#     print(f'x: {x}, y: {y}, z: {z}')
#     print(f'args: {args}')

# function(1, 2, 3, 4, z=5)

# def function(x, y, *args, z=10, **kwargs):
#     print(f'x: {x}, y: {y}, z: {z}')
#     print(f'args: {args}')
#     print(f'kwargs: {kwargs}')

# function(1, 2, 3, 4, a=100, b=200)

# t = (3, 4, 5)
# a = t[0]
# b = t[1]
# c = t[2]
# print(a, b, c)

# t = (3, 4, 5)
# a, b, c = t
# print(a, b, c)

# t = (3, 4, 5, 6, 7, 8)
# a, b, c, *d = t
# print(a, b, c, d)

# t = (3, 4, 5, 6, 7, 8)
# a, b, c, *_ = t
# print(a, b, c, _)

l = [1, 2, 3]
d = {'d1': 10, 'd2': 20}

def function(x, y, z):
    print(f'x: {x}, y: {y}, z: {z}')

function(l[0], l[1], l[2])

function(*l)

def function(x, y, z, d1 = 0, d2 = 0):
    print(f'x: {x}, y: {y}, z: {z}, d1: {d1}, d2: {d2}')

function(1, 2, 3, d1=d['d1'], d2=d['d2'])

function(1, 2, 3, **d)

def function(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')

function(*l, **d)