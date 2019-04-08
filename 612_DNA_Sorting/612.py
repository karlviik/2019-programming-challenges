# create alphabet dict with lower value being at the front-er end of alphabet
alphabet = {
    "A": 1,
    "C": 2,
    "G": 3,
    "T": 4
}
# get number of cases
cases = int(input())
# for each case
for a in range(cases):
    # get the empty line
    input()
    # get num of strings, len of strings is not needed
    rule = int(input().split()[1])
    # create list
    allYall = []
    # for each string
    for i in range(rule):
        # get the line
        line = input()
        # unsortedness int
        recc = 0
        # table that holds count of letters (a, c, g, t)
        table = [0, 0, 0, 0]
        # for each letter in the line
        for x in line:
            # for each letter that is "above" the letter
            # like for each letter that before current letter x would count as unsorted
            for y in range(alphabet[x], 4):
                # add the count of those letters to unsortedness int
                recc += table[y]
            # add the letter to that letter's table slot
            table[alphabet[x] - 1] += 1
        # add it to list as list of the string and sortedness count
        allYall.append([line, recc])
    # sort the list, will keep order if same unsortedness
    allYall = sorted(allYall, key=lambda x: x[1])
    # print them out
    for o in allYall:
        print(o[0])
    # if not last case, print empty line
    if a != cases - 1:
        print()
