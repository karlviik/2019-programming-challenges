while True:
    nodes = int(input())
    if nodes == 0:
        exit()
    edges = int(input())
    nodepairs = []
    alreadyvisited = []
    groups = {}
    shouldend = False
    for i in range(edges):
        inputs = list(map(int, input().split()))
        if shouldend:
            continue
        if i == 0:
            groups[inputs[0]] = 0
            groups[inputs[1]] = 1
            alreadyvisited.append(inputs[0])
            alreadyvisited.append(inputs[1])
        else:
            if alreadyvisited.__contains__(inputs[0]):
                othergroup = (groups[inputs[0]] + 1) % 2
                if alreadyvisited.__contains__(inputs[1]):
                    if groups[inputs[1]] != othergroup:
                        print("NOT BICOLORABLE.")
                        shouldend = True
                        continue
                groups[inputs[1]] = othergroup
                alreadyvisited.append(inputs[1])

            elif alreadyvisited.__contains__(inputs[1]):
                othergroup = (groups[inputs[1]] + 1) % 2
                groups[inputs[1]] = othergroup
                alreadyvisited.append(inputs[0])

            else:
                nodepairs.append(inputs)
    if shouldend:
        continue
    while True:
        nodepairsnew = []
        nodepairsnew += nodepairs
        nodepairs = []
        for one, two in nodepairsnew:
            if alreadyvisited.__contains__(one):
                othergroup = (groups[one] + 1) % 2
                if alreadyvisited.__contains__(two):
                    if groups[two] != othergroup:
                        print("NOT BICOLORABLE.")
                        shouldend = True
                        break
                groups[two] = othergroup
                alreadyvisited.append(two)

            elif alreadyvisited.__contains__(two):
                othergroup = (groups[two] + 1) % 2
                groups[two] = othergroup
                alreadyvisited.append(one)
            else:
                nodepairs.append([one, two])
        if len(nodepairs) == 0:
            break
    print("BICOLORABLE.")
