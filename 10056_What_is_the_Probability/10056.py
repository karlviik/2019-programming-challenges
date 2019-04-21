testcases = int(input())
for _ in range(testcases):
    line = input()
    line = line.split()
    n = int(line[0])
    p = float(line[1])
    if p == 0:
        print("0.0000")
        continue
    i = int(line[2])
    q = 1 - p
    answer = round((q ** (i - 1)) * p * (1 / (1 - q ** n)), 4)
    print("{0:.4f}".format(answer))
