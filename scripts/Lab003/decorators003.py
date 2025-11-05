def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling the function.")
        result = func(*args, **kwargs)
        print("After calling the function.")
        return result
    return wrapper

@my_decorator
def function(x, y, z):
    print(f'x: {x}, y: {y}, z: {z}')

function(1, 2, 3)