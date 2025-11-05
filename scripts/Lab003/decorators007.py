# class FunctionObject:
#     def __call__(self, x, y):
#         print(f'FunctionObject called with arguments: {x}, {y}')

# o = FunctionObject()

# o(10, 20)

class ObjectDecorator:
    def __init__(self, func):
        self.func = func
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        print("Before calling the function.")
        result = self.func(*args, **kwargs)
        print("After calling the function.")
        return result
    
@ObjectDecorator
def function(x, y):
    print(f'x: {x}, y: {y}')

# function = ObjectDecorator(function)

function(1, 2)
function(3, 4)
function(3, 4)
function(3, 4)
print(f'Function was called {function.counter} times.')
