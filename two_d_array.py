from numpy import array
from numpy.ma.core import diagonal
from numpy.matrixlib.defmatrix import matrix

arr = array([
    [1, 2, 3, 14, 15, 16],
    [4, 5, 6, 7, 8, 9]
])

# 2d to 1d
arr1 = arr.flatten()

print(arr1)

# 1d to 3d
arr3 = arr1.reshape(2, 2, 3)
print(arr3)

arr4 = array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

m = matrix('1 2 3; 4 5 6 ; 7 8 9')
print(m)
print(diagonal(m))


m1 = matrix('1 2 3; 4 5 6; 7 8 9')
m2 = matrix('10 11 12; 13 14 15; 16 17 18')

m3 = m1 * m2

print(m3)