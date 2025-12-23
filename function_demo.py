def greet():
    print('Hello')
    print('Good morning')


greet()


def add(a, b):
    return a + b


print(add(1, 2))

def add_sub(a, b):
    return a + b, a - b

result1, result2 = add_sub(1, 2)
print(result1, result2)