import math
import heapq


def distance(one, two):
    return math.sqrt((one[0] - two[0]) ** 2 + (one[1] - two[1]) ** 2)


# most definitely not from a a* guide
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


# also totally not taken from an a* guide
def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    cost_so_far = {}
    cost_so_far[(start[0], start[1])] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph[(current[0], current[1])]:
            nextcoords = next[0:2]
            nextcost = next[2]
            new_cost = cost_so_far[(current[0], current[1])] + nextcost
            if (nextcoords[0], nextcoords[1]) not in cost_so_far or new_cost < cost_so_far[(nextcoords[0], nextcoords[1])]:
                cost_so_far[(nextcoords[0], nextcoords[1])] = new_cost
                priority = new_cost + distance(goal, next)
                frontier.put(nextcoords, priority)

    return cost_so_far


testcases = int(input())
input()
for case in range(testcases):

    # get line with home + school coords and put to vars
    homeandschool = input().split()
    home = [int(homeandschool[0]), int(homeandschool[1])]
    school = [int(homeandschool[2]), int(homeandschool[3])]

    # take in all the lines
    subwaylines = []
    # may get problems with input
    try:
        line = input()
        while line != "":
            subwaylines.append(line)
            line = input()
    except:
        _ = 0

    # nodemap should be key: [x, y], value [[x, y, cost]]
    nodemap = {}

    # populate nodemap with subway station routes
    for subwayline in subwaylines:
        subwayline = subwayline.split()
        laststop = []
        i = 0
        while i < len(subwayline) - 3:
            stop = [int(subwayline[i]), int(subwayline[i + 1])]
            if (stop[0], stop[1]) not in nodemap.keys():
                nodemap[(stop[0], stop[1])] = []
            i += 2
            if len(laststop) != 0:
                laststop.append(distance(laststop, stop))
                nodemap[(stop[0], stop[1])].append(laststop)
            if i < len(subwayline) - 3:
                nextstop = [int(subwayline[i]), int(subwayline[i + 1])]
                nextstop.append(distance(stop, nextstop))
                nodemap[(stop[0], stop[1])].append(nextstop)
                laststop = stop

    # populate the node map with missing edges
    # them being walking from each place to each other place
    allstops = nodemap.keys()
    nodemap[(school[0], school[1])] = []
    if (home[0], home[1]) not in allstops:
        nodemap[(home[0], home[1])] = []
        allstops = nodemap.keys()

    for key in allstops:
        target = [key[0], key[1], distance(home, key) * 4]
        nodemap[(home[0], home[1])].append(target)
        target = [school[0], school[1], distance(school, key) * 4]
        nodemap[(key[0], key[1])].append(target)
        for otherkey in allstops:
            if otherkey != key:
                target = [otherkey[0], otherkey[1], distance(otherkey, key) * 4]
                nodemap[(key[0], key[1])].append(target)
    # do the thing
    print(round(a_star_search(nodemap, home, school)[(school[0], school[1])] / 40000 * 60))
    if case < testcases - 1:
        print()
