from array import array
from typing import MutableSequence


def selection_sort(nums: MutableSequence[int]) -> MutableSequence[int]:
    if len(nums) <= 1:
        return nums
    for i in range(len(nums)):
        min_idx: int = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        if min_idx != i:
            nums[min_idx], nums[i] = nums[i], nums[min_idx]
    return nums


arr = array("i", [42, 17, 8, 23, 56, 4, 31, 19, 12, 27])
print(selection_sort(arr))
