# possible moves
MOVES = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


# recursive function to get words
def word_wizard(already_visited: set, coord: tuple):
    # make copy of already visited and add current coord
    incremented_already_visited = already_visited.copy()
    incremented_already_visited.add(coord)

    this_letter = letters[coord[0]][coord[1]]

    # list to be returned
    return_list = [this_letter]
    # go through all possible moves
    for new_coord in possible_moves[coord]:
        # if coord hasn't been visited
        if new_coord not in already_visited:
            # go recursive on that coord, for each answer add current letter to front
            for answer in word_wizard(incremented_already_visited, new_coord):
                answer = this_letter + answer
                return_list.append(answer)
                # if answer is longer than 2 letters, add to answer set, totally clean
                if len(answer) >= 3:
                    answers_set.add(answer)
    return return_list


cases = int(input())

for x in range(cases):
    input()
    dimension = int(input())
    letters = []
    answers_set = set()
    # put the square in list
    for _ in range(dimension):
        letters.append(input())
    start_nodes = []
    possible_moves = {}

    for i in range(dimension):
        for j in range(dimension):
            current_letter = letters[i][j]
            possible_moves[(i, j)] = []
            is_start_node = True
            for i_add, j_add in MOVES:
                # get coord
                i_new = i + i_add
                j_new = j + j_add
                # if it's allowed coord
                if dimension > i_new >= 0 and dimension > j_new >= 0:
                    new_letter = letters[i_new][j_new]
                    # if letter is "bigger", then it's a possible move
                    if new_letter > current_letter:
                        possible_moves[(i, j)].append((i_new, j_new))
                    # if letter is "smaller", then the node is not a start node
                    elif new_letter < current_letter:
                        is_start_node = False
            # if node is a start node, add it to the corresponding list
            if is_start_node:
                start_nodes.append((i, j))
    # do the recursive function for each start node
    # no returned list needed because answers are added to the set in the function
    # global variables, woooo
    # don't try this at home
    for node in start_nodes:
        word_wizard(set(), node)

    # turn the answer set into a list and sort it with tuples
    answers = []
    answers.extend(answers_set)
    answers.sort(key=lambda y: (len(y), y))
    # and print
    for answer in answers:
        print(answer)
    if x != cases - 1:
        print()
