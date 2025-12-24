def smart_div(func):
    def wrapper(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return wrapper


@smart_div
def div(a, b):
    return a / b


print(div(4, 40))
print(div(6, 3))
