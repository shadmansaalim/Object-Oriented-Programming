def do_something():
    print("Inside the function do_something")

    def inner_function():
        print('Inside the function inner_function')

    inner_function()


do_something()


def first_func():
    print("Inside the function first_func")

    def second_func():
        print("Inside the function second_func")

    return second_func


first = first_func()
first()
