from math import sqrt

def is_prime(val):
    if val < 2:
        return False
    if val == 2:
        return True
    if val % 2 == 0:
        return False
    end = int(sqrt(val)) + 1
    for i in range(3, end, 2):
        if val % i == 0:
            return False
    return True

for num in range(1, 501):
    if is_prime(num):
        print(num)
