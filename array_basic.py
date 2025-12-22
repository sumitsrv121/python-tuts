from array import array

val= array('i', [])

n = int(input('Enter length of the array: '))

for i in range(n):
    val.append(int(input('Enter a number: ')))

print(val)

num = int(input('Enter a number: '))

for i in range(len(val)):
    if num == val[i]:
        print(num, " found at index ", i)
        break
else:
    print(num, " not found")