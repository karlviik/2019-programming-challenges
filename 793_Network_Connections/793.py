# get testcase count
testcases = int(input())
# deal with the empty line
input()
# for each testcase
for testcase in range(testcases):

    # get node count which is nowhere used
    l_nodes = int(input())
    # list containing all sets aka groups of connected computers
    sets = []
    # dict where each node has a set connected to it
    locations = {}
    # initialize the right/wrong counters
    rights = 0
    wrongs = 0
    # initialize line with some value
    line = "a"
    # while line isn't empty, which would mark the end of test case
    while line:
        # catch case where no empty line at the end
        try:
            # get input
            line = input()
            # if line is empty, break out to printing
            if not line:
                break
            # get command and nodes
            comm, a, b = line.split(" ")
            # turn to ints
            a, b = int(a), int(b)
            # make so b is smaller
            if a > b:
                a, b = b, a
            # if it's a question
            if comm == "q":
                # if it's same, meaning connected to itself, then it's right
                if a == b:
                    rights += 1
                # otherwise
                else:
                    # if a and b have both been in locs and both are in same set of nodes
                    if a in locations and b in locations and locations[a] == locations[b]:
                        rights += 1
                    # they don't share a set
                    else:
                        wrongs += 1
            # if is a log instead of question
            else:
                # if a already has a set
                if a in locations:
                    # get its set
                    first_set = locations[a]
                    # if b is also in locations
                    if b in locations:
                        # get its set
                        other_set = locations[b]
                        # if the sets aren't same
                        if first_set != other_set:
                            # add b's elements to a's set
                            for i in other_set:
                                first_set.add(i)
                            # replace b's all sets with a's set
                            for i in other_set:
                                locations[i] = first_set
                    # if b isn't in locations
                    else:
                        # add b to the set
                        first_set.add(b)
                        # and set b's set to be that set
                        locations[b] = first_set
                # if a is not in a set
                else:
                    # if b is
                    if b in locations:
                        # add a to b's set and put a's set to be b's
                        locations[b].add(a)
                        locations[a] = locations[b]
                    # if neither of them are in set
                    else:
                        # create a set with both of them
                        new_set = set()
                        new_set.add(a)
                        new_set.add(b)
                        # and put that set to both of them
                        locations[a] = new_set
                        locations[b] = new_set
        # is caught, print out the results and no empty line and quit
        except Exception as e:
            print(str(rights) + "," + str(wrongs))
            quit()
    # line is empty, print out the results and empty line
    print(str(rights) + "," + str(wrongs))
    print()
