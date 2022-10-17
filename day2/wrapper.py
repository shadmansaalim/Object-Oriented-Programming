# def do_something(x, y):
#     print(f'x: {x}, y: {y}')


# do_something(12, 45)
# do_something('C++', 'Python')

def do_something(work):
    print('Started')
    work()
    print('Ended')


def practice_coding():
    print("I am learning OOP concepts and Python")


def learning_dsa():
    print("Learning Data Structures & Algorithms")


do_something(practice_coding)
do_something(learning_dsa)
