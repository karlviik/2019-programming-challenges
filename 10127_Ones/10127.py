from sys import stdin

for Input in stdin:
    if Input == "":
        break

    # create int with just ones that's definitely smaller than input
    # input length includes newline character
    i_len = len(Input) - 1
    i = 1
    for k in range(1, i_len):
        i += 10 ** k

    Input = int(Input)
    # just keep trying until get answer
    while i % Input != 0:
        i += 10 ** i_len
        i_len += 1
    print(i_len)
