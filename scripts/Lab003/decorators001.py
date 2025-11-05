from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@my_decorator
def function():
    print('Hello, World!')

#function = my_decorator(function)

function()
print(function.__name__)