x = 10
y = 20

print('x= ' + str(x) + ' y = ' + str(y))

x = x + y
y = x - y
x = x - y

print('x= ' + str(x) + ' y = ' + str(y))

x = x ^ y
y = x ^ y
x = x ^ y

print('x= ' + str(x) + ' y = ' + str(y))

x, y = y, x

print('x= ' + str(x) + ' y = ' + str(y))
