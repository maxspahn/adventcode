startNum = [int(val) for val in open("input.txt", 'r').read()[:-1].split(',')]

def step(saidNums, startNums):
    i = len(saidNums)
    if i < len(startNums):
        saidNums.append(startNums[i])
    else:
        isFound = False
        for (j, val) in enumerate(reversed(saidNums[:-1])):
            if val == saidNums[-1]:
                isFound = True
                saidNums.append(j+1)
                break
        if not isFound:
            saidNums.append(0)

    return saidNums

def stepDict(lastTimeSaid, i, lastNum):
    if lastNum not in lastTimeSaid.keys():
        num = 0
    else:
        num = i - lastTimeSaid[lastNum]
    lastTimeSaid[lastNum] = i
    return (num, lastTimeSaid)

saidNums = [startNum[0]]

lastTimeSaid = {}
for (i, val) in enumerate(startNum[:-1]):
    lastTimeSaid[val] = i

print(lastTimeSaid)

index = 2020
index = 30000000
lastNum = startNum[-1]
for i in range(len(startNum)-1, index-1):
    (lastNum, lastTimeSaid) = stepDict(lastTimeSaid,i, lastNum)

print(lastNum)



