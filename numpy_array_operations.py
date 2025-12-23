from  numpy import array
arr = array([1, 2, 3, 4])

arr += 5
print(arr)



arr1 = array([1, 2, 3, 4])
arr2 = array([5, 6, 7, 8])

arr3 = arr1 + arr2
print(arr3)



arr4 = array([10, 20, 30, 40])
arr5 = array(arr4)
print(arr5)
print(id(arr5))
print(id(arr4))
print(id(arr4) == id(arr5))
