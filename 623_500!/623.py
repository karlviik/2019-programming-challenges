from sys import stdin

# pregenerate the list
fac = [1]
for i in range(1, 1001):
    fac.append(fac[-1] * i)

# just get the answer from the list
for line in stdin:
    line = int(line)
    print(f"{line}!")
    print(fac[int(line)])
