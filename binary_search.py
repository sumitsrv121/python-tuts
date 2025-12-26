from array import array


def binary_search(nums: array, x: int, start: int, end: int) -> int:
    if start > end:
        return -1
    mid = start + (end - start) // 2

    if nums[mid] == x:
        return mid
    elif nums[mid] < x:
        return binary_search(nums, x, mid + 1, end)
    else:
        return binary_search(nums, x, start, mid - 1)


arr = array(
    "i",
    [
        3,
        7,
        12,
        18,
        21,
        25,
        29,
        33,
        38,
        42,
        47,
        51,
        56,
        60,
        64,
        69,
        73,
        77,
        82,
        86,
        91,
        95,
        99,
        104,
        108,
        112,
        117,
        121,
        125,
        130,
        134,
        138,
        143,
        147,
        151,
        156,
        160,
        164,
        169,
        173,
        178,
        182,
        186,
        191,
        195,
        199,
        204,
        208,
        212,
        217,
        221,
        225,
        230,
        234,
        238,
        243,
        247,
        251,
        256,
        260,
        265,
        269,
        273,
        278,
        282,
        286,
        291,
        295,
        299,
        304,
        308,
        312,
        317,
        321,
        325,
        330,
        334,
        338,
        343,
        347,
        352,
        356,
        360,
        365,
        369,
        373,
        378,
        382,
        386,
        391,
    ],
)


print(binary_search(arr, 257, 0, len(arr) - 1))
