num = input("Enter a number: ")

if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")
else:
    print(num, "is not a number")

if num == 1 or num == 2 or num == 3:
    print("num is ", num)
elif num == 4 or num == 5 or num == 6:
    print("num has increased and have value ", num)
else:
    print("num is ", num)
