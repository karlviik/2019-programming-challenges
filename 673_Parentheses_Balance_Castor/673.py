count = input()
for _ in range(int(count)):
    sequence = input()
    if len(sequence) % 2 == 1:
        print("No")
        continue
    elif len(sequence) == 0:
        print("Yes")
        continue
    while True:
        temp = sequence
        sequence = sequence.replace("[]", "")
        sequence = sequence.replace("()", "")
        if sequence == temp or len(sequence) == 1:
            print("No")
            break
        if len(sequence) == 0:
            print("Yes")
            break
