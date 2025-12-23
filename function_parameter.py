def add(a, b):
    c = a + b
    print(c)


add(5, 6)


def person(name, age=25):
    print('Name ', name, ', Age ', age)


person('John')


def add(*args):
    total_sum = 0
    for val in args:
        total_sum += val
    return total_sum


print(add(1, 2, 3, 4, 5, 6))
