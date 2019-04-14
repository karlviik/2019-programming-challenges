from sys import stdin

# create the list of all fibonacci numbers in the range used by the test
# thanks, python, for handling big numbers for me
fib = [0, 1]
for _ in range(5000):
    fib.append(fib[-1] + fib[-2])

# just get the answer from pregenerated list
for line in stdin:
    n = int(line)
    print(f"The Fibonacci number for {n} is {fib[n]}")

