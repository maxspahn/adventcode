import copy
def getNeighbors(row, col, lenRow, lenCol):
    n = []
    if row > 0 and row < lenRow -1 and col > 0 and col < lenCol -1:
        n = [(row-1, col), (row-1, col+1), (row-1, col-1), (row+1, col), (row+1, col-1), (row+1, col+1), (row, col+1), (row, col-1)]
    elif row > 0 and row < lenRow -1 and col == 0:
        n = [(row-1, col), (row-1, col+1), (row+1, col), (row+1, col+1), (row, col+1)]
    elif row > 0 and row < lenRow -1 and col == lenCol - 1:
        n = [(row-1, col), (row-1, col-1), (row+1, col), (row+1, col-1), (row, col-1)]
    elif row == 0 and col > 0 and col < lenCol -1:
        n = [(row+1, col), (row+1, col-1), (row+1, col+1), (row, col+1), (row, col-1)]
    elif row == lenRow - 1 and col > 0 and col < lenCol -1:
        n = [(row-1, col), (row-1, col-1), (row-1, col+1), (row, col+1), (row, col-1)]
    elif row == lenRow - 1 and col == lenCol -1:
        n = [(row-1, col), (row-1, col-1), (row, col-1)]
    elif row == 0 and col == 0:
        n = [(row+1, col), (row+1, col+1), (row, col+1)]
    return n

def getNeighborsPart2(room, row, col, lenRow, lenCol):
    n = []
    p = (row, col)
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]
    for dir in dirs:
        np = (p[0] + dir[0], p[1] + dir[1])
        while np[0] >= 0 and np[1] >= 0 and np[0] < lenRow and np[1] < lenCol:
            n.append(np)
            if not(room[np[0]][np[1]] == 2):
                break
            np = (np[0] + dir[0], np[1] + dir[1])
    return n

def getNewState(room, row, col):
    lenRow = len(room)
    lenCol = len(room[0])
    occ = 0
    if room[row][col] == 1:
        occ = 1
    elif room[row][col] == 0:
        occ = 0
    elif room[row][col] == 2:
        occ = 0
    n = getNeighbors(row, col, lenRow, lenCol)
    if room[row][col] == 2:
        return (2, 0)
    nbOcc = 0
    for seat in n:
        if room[seat[0]][seat[1]] == 1:
            nbOcc += 1
    if nbOcc == 0 and room[row][col] == 0:
        return (1, 1)
    elif nbOcc >= 4 and room[row][col] == 1:
        return (0, 0)
    return (room[row][col], occ)

def getNewStatePart2(room, row, col):
    lenRow = len(room)
    lenCol = len(room[0])
    occ = 0
    if room[row][col] == 1:
        occ = 1
    elif room[row][col] == 0:
        occ = 0
    elif room[row][col] == 2:
        occ = 0
    n = getNeighborsPart2(room, row, col, lenRow, lenCol)
    if room[row][col] == 2:
        return (2, 0)
    nbOcc = 0
    for seat in n:
        if room[seat[0]][seat[1]] == 1:
            nbOcc += 1
    if nbOcc == 0 and room[row][col] == 0:
        return (1, 1)
    elif nbOcc >= 5 and room[row][col] == 1:
        return (0, 0)
    return (room[row][col], occ)

def step(room):
    new_room = copy.deepcopy(room)
    totOcc = 0
    for i in range(len(room)):
        for j in range(len(room[0])):
            (new_room[i][j], occ) = getNewState(room, i, j)
            totOcc += occ
    return (new_room, totOcc)

def stepPart2(room):
    new_room = copy.deepcopy(room)
    totOcc = 0
    for i in range(len(room)):
        for j in range(len(room[0])):
            (new_room[i][j], occ) = getNewStatePart2(room, i, j)
            totOcc += occ
    return (new_room, totOcc)

file = open('input.txt', 'r')

room = []
mapping = {'L':0, '.':2, '#':1}
for i, line in enumerate(file):
    row = [mapping[c] for c in line[:-1]]
    room.append(row)

totOccOld = -1
newOcc = 0
counter = 0
while totOccOld != newOcc:
    counter += 1
    totOccOld = newOcc
    (room, newOcc) = stepPart2(room)

print(newOcc)
