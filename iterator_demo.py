nums = [6, 7, 8, 5]

itr = iter(nums)

num = next(itr, None)

while num is not None:
    print(num)
    num = next(itr, None)


class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        val = self.num
        if self.num <= 10:
            self.num += 1
        else:
            raise StopIteration()
        return val


tt = TopTen()
for i in tt:
    print(i)
