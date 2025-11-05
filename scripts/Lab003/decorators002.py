def my_decorator(func):
    print("Decorating the function.")
    return func

@my_decorator
def function():
    print('Hello, World!')

# function = my_decorator(function)

function()
function()
function()
function()