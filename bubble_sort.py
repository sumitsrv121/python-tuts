from array import array
from typing import MutableSequence


def bubble_sort(nums: MutableSequence[int]) -> MutableSequence[int]:
    for i in range(len(nums)):
        swapped: bool = False
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums


arr = array("i", [42, 17, 8, 23, 56, 4, 31, 19, 12, 27])
print(bubble_sort(arr))
