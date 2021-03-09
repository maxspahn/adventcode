import os
file = open('input.txt', 'r')

groups = file.read().split(2*os.linesep)
totalCount = 0
totalCountPart2 = 0
for i, group in enumerate(groups):
    letterDict = {}
    part2Dict = {}
    nbPersons = len(group.splitlines())
    for char in group:
        if char == '\n':
            continue
        letterDict[char] = True
        if char in part2Dict.keys():
            part2Dict[char] += 1
        else:
            part2Dict[char] = 1
    for val in part2Dict.values():
        if val == nbPersons:
            totalCountPart2 += 1
    totalCount += len(letterDict)

print("Part 1: ", totalCount)
print("Part 2: ", totalCountPart2)
