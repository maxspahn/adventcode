file = open("input.txt", "r")

## read in data
boolLines = []
for line in file:
    boolLine = []
    for c in line:
        if c == '#':
            boolLine.append(1)
        elif c == '.':
            boolLine.append(0)
    boolLines.append(boolLine)

## Part 1
pos = [0, 0]
slope = [3, 1]
treesCounter = 0
while pos[1] < len(boolLines):
    if boolLines[pos[1]][pos[0]]:
        treesCounter += 1
    pos[0] += slope[0]
    pos[1] += slope[1]
    pos[0] = pos[0] % len(boolLine)

print("Part 1 : # Trees encountered", treesCounter)

## Part 2

product = 1
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
for slope in slopes:
    pos = [0, 0]
    treesCounter = 0
    while pos[1] < len(boolLines):
        if boolLines[pos[1]][pos[0]]:
            treesCounter += 1
        pos[0] += slope[0]
        pos[1] += slope[1]
        pos[0] = pos[0] % len(boolLine)

    print("Slope " + str(slope) + " : # Trees encountered", treesCounter)
    product *= treesCounter

print("Answer Part 2 : " + str(product))




file.close()
