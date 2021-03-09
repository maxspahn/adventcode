import copy

def getN(pos):
    neighs = []
    dirs = [-1, 0, 1]
    for i in dirs:
        for j in dirs:
            for k in dirs:
                if i == 0 and j == 0 and k == 0:
                    continue
                neighs.append((pos[0] + i, pos[1] + j, pos[2] + k))
    return neighs

def getNPart2(pos):
    neighs = []
    dirs = [-1, 0, 1]
    for i in dirs:
        for j in dirs:
            for k in dirs:
                for l in dirs:
                    if i == 0 and j == 0 and k == 0 and l == 0:
                        continue
                    neighs.append((pos[0] + i, pos[1] + j, pos[2] + k, pos[3] + l))
    return neighs


def checkN(grid, pos):
    n = getN(pos)
    nbAct = 0
    for posN in n:
        if posN in grid:
            nbAct += 1
    return nbAct

def checkNPart2(grid, pos):
    n = getNPart2(pos)
    nbAct = 0
    for posN in n:
        if posN in grid:
            nbAct += 1
    return nbAct

def printGrid(candGridRange, grid):
    for i in range(candGridRange[2][0], candGridRange[2][1] + 1):
        print('z=', i)
        for j in range(candGridRange[1][0], candGridRange[1][1] + 1):
            for k in range(candGridRange[0][0], candGridRange[0][1] + 1):
                if (k, j, i) in grid:
                    print('#', end='')
                else:
                    print('.', end='')
            print()

def printGridPart2(candGridRange, grid):
    for l in range(candGridRange[3][0], candGridRange[3][1] + 1):
        for i in range(candGridRange[2][0], candGridRange[2][1] + 1):
            print('w=', l)
            print('z=', i)
            for j in range(candGridRange[1][0], candGridRange[1][1] + 1):
                for k in range(candGridRange[0][0], candGridRange[0][1] + 1):
                    if (k, j, i, l) in grid:
                        print('#', end='')
                    else:
                        print('.', end='')
                print()

file = open('input.txt', 'r')
grid = []
for i, line in enumerate(file):
    for j, val in enumerate(line):
        if val == '#':
            grid.append((j, i, 0))

candGridRange = [[0, 7], [0, 7], [0, 0]]
candPos = []
for i in range(candGridRange[0][0], candGridRange[0][1] + 1):
    for j in range(candGridRange[1][0], candGridRange[1][1] + 1):
        for k in range(candGridRange[2][0], candGridRange[2][1] + 1):
            candPos.append((i, j, k))


for i in range(6):
    for j in range(3):
        candGridRange[j][0] -= 1
        candGridRange[j][1] += 1
    candPos = []
    for i in range(candGridRange[0][0], candGridRange[0][1] + 1):
        for j in range(candGridRange[1][0], candGridRange[1][1] + 1):
            for k in range(candGridRange[2][0], candGridRange[2][1] + 1):
                candPos.append((i, j, k))
    newGrid = copy.deepcopy(grid)
    for cand in candPos:
        nbAct = checkN(grid, cand)
        if nbAct == 3 and cand not in grid:
            newGrid.append(cand)
        elif nbAct == 2 or nbAct ==3 and cand in grid:
            continue
        elif cand in grid:
            newGrid.remove(cand)
    grid = newGrid
    #printGrid(candGridRange, newGrid)

print(len(grid))

file.seek(0)
grid = []
for i, line in enumerate(file):
    for j, val in enumerate(line):
        if val == '#':
            grid.append((j, i, 0, 0))

#candGridRange = [[0, 2], [0, 2], [0, 0], [0, 0]]
candGridRange = [[0, 7], [0, 7], [0, 0], [0, 0]]
candPos = []
for i in range(candGridRange[0][0], candGridRange[0][1] + 1):
    for j in range(candGridRange[1][0], candGridRange[1][1] + 1):
        for k in range(candGridRange[2][0], candGridRange[2][1] + 1):
            for l in range(candGridRange[3][0], candGridRange[3][1] + 1):
                candPos.append((i, j, k, l))


print(len(getNPart2(candPos[0])))
for i in range(6):
    print("run : " , i)
    for j in range(4):
        candGridRange[j][0] -= 1
        candGridRange[j][1] += 1
    candPos = []
    for i in range(candGridRange[0][0], candGridRange[0][1] + 1):
        for j in range(candGridRange[1][0], candGridRange[1][1] + 1):
            for k in range(candGridRange[2][0], candGridRange[2][1] + 1):
                for l in range(candGridRange[3][0], candGridRange[3][1] + 1):
                    candPos.append((i, j, k, l))
    #printGridPart2(candGridRange, grid)
    newGrid = copy.deepcopy(grid)
    for cand in candPos:
        nbAct = checkNPart2(grid, cand)
        if nbAct == 3 and cand not in grid:
            newGrid.append(cand)
        elif nbAct == 2 or nbAct ==3 and cand in grid:
            continue
        elif cand in grid:
            newGrid.remove(cand)
    grid = newGrid
    #printGrid(candGridRange, newGrid)

print(len(grid))








