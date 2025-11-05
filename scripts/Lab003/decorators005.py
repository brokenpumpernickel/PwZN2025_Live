def my_decorator(func = None, a = 0, b = 0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator parameters: a={a}, b={b}")
            print("Before calling the function.")
            result = func(*args, **kwargs)
            print("After calling the function.")
            return result
        return wrapper

    if func is not None:
        return decorator(func)
    return decorator

# @my_decorator(a=5, b=10)
# def function(x, y, z):
#     print(f'x: {x}, y: {y}, z: {z}')

# function = my_decorator(a=5, b=10)(function)

# function(1, 2, 3)

@my_decorator
def function(x, y, z):
    print(f'x: {x}, y: {y}, z: {z}')

function = my_decorator(function)

function(1, 2, 3)