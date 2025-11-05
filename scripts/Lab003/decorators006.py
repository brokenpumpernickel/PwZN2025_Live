import time
from functools import cache

@cache
def fibon(n):
    if n < 2:
        return n
    return fibon(n - 1) + fibon(n - 2)

start = time.time()
for i in range(42):
    print(i, fibon(i))
stop = time.time()
print(stop - start)