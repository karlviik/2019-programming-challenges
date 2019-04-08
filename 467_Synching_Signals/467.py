from sys import stdin

set = 0

for line in stdin:

    set += 1
    times = list(map(int, line.split()))

    # simulate through all seconds
    for sec in range(2 * min(times), 3601):
        # if second has all things green
        if all(sec % (x * 2) < x - 5 for x in times):
            print(f"Set {set} synchs again at {sec // 60} minute(s) and {sec % 60} second(s) after all turning green.")
            break
    else:
        print(f"Set {set} is unable to synch after one hour.")
