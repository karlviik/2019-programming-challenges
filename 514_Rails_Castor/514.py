while True:
    n = int(input())
    if n == 0:
        break
    while True:
        line = input()
        if line == "0":
            break

        m = 0
        req = line.split()
        stack = [0]
        for element in req:
            num = int(element)
            if num < stack[-1]:
                print("No")
                break
            elif num == stack[-1]:
                stack.pop(-1)
            elif num > stack[-1]:
                if num < m:
                    print("No")
                    break
                while True:
                    m += 1
                    if m != num:
                        stack.append(m)
                    else:
                        break
            if len(stack) == 1 and m == n:
                print("Yes")
    print("")


