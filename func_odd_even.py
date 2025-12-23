def odd_even(nums=None):
    if nums is None:
        nums = []
    odd_nums = []
    even_nums = []
    for num in nums:
        if num % 2 != 0:
            odd_nums.append(num)
        else:
            even_nums.append(num)
    return odd_nums, even_nums

lst = []
n = int(input('Enter total number of elements: '))

for i in range(n):
    lst.append(int(input('Enter element: ')))

odd_lst, even_lst = odd_even(lst)
print(odd_lst)
print(even_lst)
