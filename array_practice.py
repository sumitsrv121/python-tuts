from array import array

vals = array('i', [5, 9, 8, 4, 2])
print(vals)
print(vals.buffer_info())


for num in vals:
    print(num)

vals_copy = array(vals.typecode, (a for a in vals))
print(vals_copy)
