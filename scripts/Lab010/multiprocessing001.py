import time
import functools
import numba
import multiprocessing
import concurrent.futures
from concurrent.futures import ProcessPoolExecutor, as_completed

#@functools.cache
#@numba.njit
def fibon(n):
    if n < 2:
        return n
    return fibon(n - 1) + fibon(n - 2)

if __name__ == "__main__":
    # start = time.time()
    # for i in range(40):
    #     print(i, fibon(i))
    # end = time.time()
    # print("Time taken:", end - start)

    # print(f'Number of CPU cores: {multiprocessing.cpu_count()}')

    start = time.time()
    with ProcessPoolExecutor(multiprocessing.cpu_count()) as executor:
        results = [executor.submit(fibon, n) for n in range(39, -1, -1)]
        for future in as_completed(results):
            print(future.result())
    end = time.time()
    print("Time taken:", end - start)