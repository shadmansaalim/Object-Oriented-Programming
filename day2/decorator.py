import math
import time


def timer(func):
    def inner(*args, **kwargs):
        print('Time Start')
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'Time End : Time Took For Execution {end-start}')
    return inner


@timer
def get_factorial(n):
    result = math.factorial(n)
    print(f'Factorial of {n} is {result}')


# timer(get_factorial)()

# Working because of *args
get_factorial(5)

# We can do this only because in the above inner function inside timmer function we wrote **kwargs as argument which basically means multiple keyword arguments
get_factorial(n=5)


# Because of adding @timer above get_factorial the timer function is called with the parameter get_factorial function
