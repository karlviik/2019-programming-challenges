from statistics import median

Num_inputs = int(input())
for _ in range(Num_inputs):
    Line = list(map(lambda x: int(x), input().split()))
    # get median from the houses, median is right in the "middle" so it'll give best location
    Median = median(Line[1:])
    Sum = 0
    for thing in Line[1:]:
        Sum += abs(thing - Median)
    print(int(round(Sum)))
