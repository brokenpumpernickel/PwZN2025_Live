def my_generator():
    yield 'Hello'
    yield 'World'
    yield 'from'
    yield 'the'
    yield 'generator!'

for word in my_generator():
    print(word)

def my_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

for number in my_range(5):
    print(number)

print(list(my_range(10)))