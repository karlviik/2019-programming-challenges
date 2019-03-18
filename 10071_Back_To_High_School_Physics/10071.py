from sys import stdin

for line in stdin:
    if line == '':
        break
    line = line.split()
    print(int(line[0]) * int(line[1]) * 2)
