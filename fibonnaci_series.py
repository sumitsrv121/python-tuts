def fibonacci_series(num):
    if num <= 0:
        return []
    first, second = 0, 1
    fib_lst = [first, second]
    for n in range(2, num):
        first, second = second, first + second
        fib_lst.append(second)
    return fib_lst

print(fibonacci_series(10))