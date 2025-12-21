a = int(input('Enter a number: '))
b = int(input('Enter another number: '))
c = int(input('Enter another number: '))

if a > b:
    if a > c:
        print(a, " is the greatest.")
    else:
        print(c, " is the greatest.")
elif b > c:
    print(b, " is the greatest.")
else:
    print(c, " is the greatest.")