testcases = int(input())
# part of trying to get rid of an error
if testcases == 0:
    quit()
input()

# for each testcase
for x in range(testcases):
    heightlist = []
    # get in all the heights with try except to catch end of file error
    try:
        while True:
            height = input()
            if height == "":
                break
            else:
                heightlist.append(int(height))
    except:
        _ = "wasd"
    numberOfHits = {}
    listOfHits = {}
    # totalbest to not need to iterate through them again
    totalBest = -float("inf")
    totalBestIndex = ""
    # for each i for heightlist index starting from back
    for i in range(len(heightlist) - 1, -1, -1):
        # initiate list of hits and number of hits with itself
        listOfHits[i] = [heightlist[i]]
        numberOfHits[i] = 1
        # get the height of the current spot
        height = heightlist[i]
        # best to get best option after this missile
        best = -float('inf')
        bestIndex = ""
        # for each height after this one
        for j in range(i + 1, len(heightlist)):
            # if this one is higher AND has more hits than best
            if heightlist[j] > height and best < numberOfHits[j]:
                # mark it as best
                best = numberOfHits[j]
                bestIndex = j
        # if there is a best, add it to listofhits and numofhits
        # of current one
        if bestIndex != "":
            listOfHits[i] += listOfHits[bestIndex]
            numberOfHits[i] += numberOfHits[bestIndex]
        # if the number of hits is better than totalbest, make it the
        # current totalbest
        if numberOfHits[i] > totalBest:
            totalBest = numberOfHits[i]
            totalBestIndex = i
    # print amount of hits and all of the hits
    print(f"Max hits: {totalBest}")
    if totalBestIndex != "":
        for hit in listOfHits[totalBestIndex]:
            print(hit)
    # newline just between testcases
    if x != testcases - 1:
        print()
