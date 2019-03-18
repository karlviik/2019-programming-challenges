from itertools import permutations

count = int(input())
for _ in range(count):
    stringPermutations = sorted(set([''.join(p) for p in permutations(sorted(input()))]))
    for string in stringPermutations:
        print(string)
    print()
