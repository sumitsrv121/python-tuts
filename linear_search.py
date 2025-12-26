from array import array
from cmath import inf

arr = array("i", [5, 8, 4, 6, 9, 2])

val = -9

for i in range(len(arr)):
    if arr[i] == val:
        print(i)
        break
else:
    print(-inf)
