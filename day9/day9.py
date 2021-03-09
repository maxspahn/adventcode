import numpy as np
file = open('input.txt', 'r')

N = 25
n = 1000
numbers = np.empty(n, dtype='uint')
sums = np.empty(shape=(n, n), dtype='uint')
newSums = np.empty(shape=(n), dtype='uint')

for i, line in enumerate(file):
    numbers[i] = int(line)

num = np.tile(numbers, (n, 1))
sums = np.add(num, np.transpose(num))

for i, val in enumerate(numbers):
    if i < N:
        continue
    sel = sums[i-N:i, i-N:i]
    if val not in sel:
        badVal = val 
        break

print("Part Result 1 :", badVal)

isFound = False
for i in range(len(numbers)):
    if isFound:
        break
    cand = 0
    for j in range(i, len(numbers)):
        cand += numbers[j]
        if cand == badVal:
            print("Part Result 2 :", min(numbers[i:j]) + max(numbers[i:j]))
            isFound = True
            break
        elif cand > badVal:
            break



