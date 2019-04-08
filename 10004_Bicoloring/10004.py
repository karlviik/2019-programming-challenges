# for each test case
while True:
    # get amount of nodes in graph
    nodes = int(input())
    # if is 0, then exit as it marks the end of input
    if nodes == 0:
        exit()
    # get number of edges in graph
    edges = int(input())
    # create lists and a dict
    nodepairs = []
    alreadyvisited = []
    groups = {}
    # create a boolean for skipping in case not bicolorable
    shouldend = False
    # for each edge
    for i in range(edges):
        # take the 2 numbers in as a list of ints
        inputs = list(map(int, input().split()))
        # if no point of calcing, just skip to read next input
        if shouldend:
            continue
        # if is the first loop
        if i == 0:
            # put the first node into dict to be group 0
            groups[inputs[0]] = 0
            # and second to be group 1
            groups[inputs[1]] = 1
            # add both nodes to alreadyvisited list
            alreadyvisited.append(inputs[0])
            alreadyvisited.append(inputs[1])
        # otherwise
        else:
            # if have already passed the first node
            if alreadyvisited.__contains__(inputs[0]):
                # create int that would correspond to other node's group
                othergroup = (groups[inputs[0]] + 1) % 2
                # if the other node has also been visited
                if alreadyvisited.__contains__(inputs[1]):
                    # and if the groups don't match up
                    if groups[inputs[1]] != othergroup:
                        # print not colorable and start skipping loops
                        print("NOT BICOLORABLE.")
                        shouldend = True
                        continue
                # could just have else here
                # add it to the proper group (othergroup) and add to already visited
                groups[inputs[1]] = othergroup
                alreadyvisited.append(inputs[1])
            # if first node hasn't been visited and second has
            elif alreadyvisited.__contains__(inputs[1]):
                # get the group for first node
                othergroup = (groups[inputs[1]] + 1) % 2
                # add to groups dict and add to already visited
                groups[inputs[1]] = othergroup
                alreadyvisited.append(inputs[0])

            else:
                # otherwise add them to the pairs list to be processed later
                nodepairs.append(inputs)
    # if no point of continuing, just skip to next text case
    if shouldend:
        continue

    while True:
        # crate new list
        nodepairsnew = []
        # and add nodepairs into it, don't remember why exactly, to clone it?
        nodepairsnew += nodepairs
        # and make nodepairs empty
        nodepairs = []
        # start cycling through the node pairs, basically same as before, bit simpler
        for one, two in nodepairsnew:
            # if have visited first
            if alreadyvisited.__contains__(one):
                # get other's group
                othergroup = (groups[one] + 1) % 2
                # if other has been visited
                if alreadyvisited.__contains__(two):
                    # and groups don't match
                    if groups[two] != othergroup:
                        # is not bicolorable and break out of for
                        print("NOT BICOLORABLE.")
                        shouldend = True
                        break
                # can also be else here
                # add the other node to alreadyvisited and put proper group
                groups[two] = othergroup
                alreadyvisited.append(two)
            # if have visited second but not first
            elif alreadyvisited.__contains__(two):
                # get first's group and add to groups and alreadyvisited
                othergroup = (groups[two] + 1) % 2
                groups[two] = othergroup
                alreadyvisited.append(one)
            # if haven't visited either, add to nodepairs for next cycle of while true
            else:
                nodepairs.append([one, two])
        # if no nodes in nodepairs or no point of continuing, break out
        if len(nodepairs) == 0 or shouldend:
            break
    # if no conflict has been detected
    if not shouldend:
        print("BICOLORABLE.")
