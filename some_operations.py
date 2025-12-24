from functools import reduce

nums = [3, 2, 6, 8, 4, 6, 2, 9]

even_nums = list(filter(lambda num: num % 2 == 0, nums))
print(even_nums)


double_even_nums = list(map(lambda num: num * 2, even_nums))
print(double_even_nums)

total_sum = reduce(lambda initial, num: num + initial, double_even_nums, 0)
print(total_sum)
