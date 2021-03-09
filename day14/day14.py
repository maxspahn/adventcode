import re

def applyValMask(val, mask):
    bitStr = list(format(val, '036b'))
    for i in range(36):
        if mask[i] == '1':
            bitStr[i] = '1'
        elif mask[i] == '0':
            bitStr[i] = '0'
    return int("".join(bitStr), 2)

def applyMemMask(add, mask):
    bitStr = list(format(add, '036b'))
    xPos = []
    listMem = []
    for i in range(36):
        if mask[i] == '1':
            bitStr[i] = '1'
        if mask[i] == 'X':
            xPos.append(i)
    f = '0' + str(len(xPos)) + 'b'
    nbPos = 2**len(xPos)
    for i in range(nbPos):
        rep = format(i, f)
        for (j, pos) in enumerate(xPos):
            bitStr[pos] = rep[j]
        listMem.append(int("".join(bitStr), 2))
    return listMem

file = open('input.txt', 'r')
p1 = re.compile('mask\s\=\s(\w*)')
p2 = re.compile('mem\[(\d*)\]\s\=\s(\d+)')


mem = {}
for line in file:
    m1 = p1.match(line)
    m2 = p2.match(line)
    if m1:
        mask = m1.group(1)
    if m2:
        mem[int(m2.group(1))] = applyValMask(int(m2.group(2)), mask)

s = 0
for key in mem.keys():
    s += mem[key]
print("Part 1 Result :", s)

mem = {}
file.seek(0)
for line in file:
    m1 = p1.match(line)
    m2 = p2.match(line)
    if m1:
        mask = m1.group(1)
    if m2:
        listMem = applyMemMask(int(m2.group(1)), mask)
        for memEntry in listMem:
            mem[memEntry] = int(m2.group(2))

s = 0
for key in mem.keys():
    s += mem[key]
print("Part 2 Result :", s)
