# for each line of the input
while True:
    # get the whole line
    line = input()
    # if is end character, break out
    if line == "#":
        break
    # get maze, minotaur location, theseus location, and candle "step"
    part1, minotaur, theseus, c = line.split()
    # turn candle step to int
    c = int(c)
    # remove the dot at end and split at dividers
    relations = part1.strip(".").split(";")
    # create list of nodes with candles
    with_candle = []
    # also a set
    with_candle_set = set()
    # create dict where each node has list of nodes it can go to
    pathways = {}
    # for each relation
    for relation in relations:
        # if has no "targets", make dict empty list
        if len(relation) <= 2:
            pathways[relation[0]] = []
        # otherwise
        else:
            # m is node, n is stringlisty thing of targets
            m, n = relation.split(":")
            pathways[m] = []
            # for each target node
            for i in n:
                # if node is not in the dict keys, add to dict,
                # for cases where the target node is not as the source in the maze string
                if i not in pathways:
                    pathways[i] = []
                # add target to list
                pathways[m].append(i)
    # start simulating
    index = 1
    while True:
        # start going through minotaur's options
        for path in pathways[minotaur]:
            # if theseus is not there and target doesn't have candle
            if path != theseus and path not in with_candle_set:
                # go there, theseus follows
                theseus, minotaur = minotaur, path
                break
        # if for detected no options, therefore minotaur is trapped
        else:
            # print list of candles + space if there are candles + where minotaur got trapped
            print(" ".join(with_candle) + (" " if with_candle_set else "") + "/" + minotaur)
            break
        # if has reached point where candle has to be dropped
        if index == c:
            # add theseus location to candle list/set and index = 1
            with_candle.append(theseus)
            with_candle_set.add(theseus)
            index = 1
        # otherwise increment candle counter
        else:
            index += 1


