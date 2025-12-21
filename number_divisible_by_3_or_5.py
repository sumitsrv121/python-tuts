counter = 1
while counter <= 100:
    if counter % 3 == 0 and counter % 5 == 0:
        print(counter, " is divisible by both 3 and 5")
    elif counter % 3 == 0:
        print(counter, " is divisible by 3")
    elif counter % 5 == 0:
        print(counter, " is divisible by 5")
    counter += 1