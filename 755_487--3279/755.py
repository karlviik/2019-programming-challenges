alphamap = {"A": "2", "B": "2", "C": "2", "D": "3", "E": "3", "F": "3", "G": "4", "H": "4", "I": "4", "J": "5", "K": "5", "L": "5", "M": "6", "N": "6", "O": "6", "P": "7", "R": "7", "S": "7", "T": "8", "U": "8", "V": "8", "W": "9", "X": "9", "Y": "9", "0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}

datasets = int(input())

for i in range(datasets):
    input()
    duplicates_set = set()
    duplicates = []
    numbers = {}
    num_count = int(input())
    # for each number put in
    for _ in range(num_count):
        number = input()
        # first get rid of dashes
        number = number.replace("-", "")
        actual_num = ""
        # build the actual number with use of alphamap dictionary
        # kinda slow because making new strings but fast enough
        for letter in number:
            actual_num += alphamap[letter]
        # add the dash
        actual_num = actual_num[0:3] + "-" + actual_num[3:]
        # if the number is already in dictionary
        if actual_num in numbers:
            # add it to the set and increment its count
            duplicates_set.add(actual_num)
            numbers[actual_num] += 1
        # otherwise create dict entry
        else:
            numbers[actual_num] = 1
    # if there are no duplicates, output the string
    if len(duplicates_set) == 0:
        print("No duplicates.")
    # otherwise put to list, sort and output
    else:
        duplicates.extend(duplicates_set)
        duplicates.sort()
        for number in duplicates:
            print(number + " " + str(numbers[number]))
    if i != datasets - 1:
        print()
