import random


def top_ten():
    for j in range(10):
        num = random.randint(1, 500)
        yield num


for i in top_ten():
    print(i)


# top ten perfect square
def top_ten_perfect_square():
    n = 1
    while n <= 10:
        yield n**2
        n += 1


print("=" * 100)
for i in top_ten_perfect_square():
    print(i)
