from math import sqrt

while True:
    Input = input()
    if Input == "0":
        break
    # if input is a square of an int, then and only then is the input
    # divisible by uneven amount of integers, therefore only then will
    # last bulb be on at the end.
    if sqrt(int(Input)) % 1 == 0:
        print("yes")
    else:
        print("no")
