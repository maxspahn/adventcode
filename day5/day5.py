import numpy as np
f = open("input.txt", "r")
ids = []
taken = np.zeros(shape=(128, 8))
for line in f:
    row = int(line.replace('B', '1').replace('F', '0')[0:7], 2)
    col = int(line.replace('R', '1').replace('L', '0')[7:10], 2)
    taken[row][col] = 1
    ids.append(row * 8 + col)

print("Maximum Seat id : ", max(ids))

for i, r in enumerate(taken):
    for j, c in enumerate(r):
        if taken[i][j] == 0:
            canId = i * 8 + j
            if (canId+1) in ids and (canId-1) in ids:
                print("Found your id : ", canId)
                break;

