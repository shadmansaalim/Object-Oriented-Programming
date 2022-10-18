# Fibonacci : 1, 1, 2, 3, 5, 8, 13, 21
from time import time
from functools import lru_cache as cache


@cache
def fibo(n):
    if (n <= 1):
        return 1
    return fibo(n-1) + fibo(n-2)


start = time()
for i in range(30):
    print(i, fibo(i))
end = time()

milli_seconds = (end-start)*1000
print(f'Took {milli_seconds} Milli Seconds to run')

# Without Cache Took 357.5890064239502 Milli Seconds to run
# With Cache Took 0.08177757263183594 Milli Seconds to run
