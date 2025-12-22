import math

for index in range(1, 501):
    if math.sqrt(index).is_integer():
        print(index, " is a perfect square")