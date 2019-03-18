import itertools
import math

while True:
    count = input()
    if count == "":
        continue
    count = int(count)
    if count == 0:
        break
    allThings = []
    for _ in range(count):
        allThings.append(int(input()))
    pairs = itertools.combinations(allThings, 2)
    thing = 0
    countOfAllThings = 0
    for pair in pairs:
        countOfAllThings += 1
        if math.gcd(pair[0], pair[1]) <= 1:
            thing += 1
    if thing == 0:
        print("No estimate for this data set.")
        continue
    print("%.6f" % round(math.sqrt(6 * countOfAllThings / thing), 6))
