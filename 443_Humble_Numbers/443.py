some_twos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
some_threes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
some_fives = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
some_sevens = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

other_list = []

for a in range(12):
    for b in range(max(1, 14 - a)):
        for c in range(max(1, 20 - a - b)):
            for d in range(max(1, 31 - a - b - c)):
                other_list.append([some_twos[d], some_threes[c], some_fives[b], some_sevens[a]])
other_list = sorted(other_list, key=lambda x: x[0] * 1 + x[1] * 1.58496 + x[2] * 2.32192 + x[3] * 2.80735)
while True:
    request = int(input())
    if request == 0:
        break
    x = other_list[request - 1]
    line = f"The {request}"
    remainder = request % 10
    longerRemainder = request % 100
    if 14 > longerRemainder > 10:
        line += "th "
    elif remainder == 1:
        line += "st "
    elif request % 10 == 2:
        line += "nd "
    elif request % 10 == 3:
        line += "rd "
    else:
        line += "th "
    print(f"{line}humble number is {2 ** x[0] * 3 ** x[1] * 5 ** x[2] * 7 ** x[3]}.")
