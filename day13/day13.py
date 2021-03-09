import re
import numpy as np

file = open('input.txt', 'r')

dep = int(file.readline())
info = file.readline()[:-1].split(',')

limit = dep + 100
nbBuses = len(info)
depTable = np.zeros(shape=(limit, nbBuses), dtype='uint')

for (i, val) in enumerate(info):
    if val =='x':
        continue
    v = int(val)
    c = v
    while c < limit:
        depTable[c][i] = 1
        c += v

i = dep
noBus = True
while noBus == True:
    for j in range(nbBuses):
        if depTable[i, j] != 0:
            trueDep = i
            idBus = int(info[j])
            noBus = False
    i += 1

diffDep = trueDep - dep
print("Result Part 1: ", diffDep * idBus)

# Part 2

def add(of1, of2,):
    f = of1[1] * of2[1]
    v = of1[0]
    o = 0
    dist = of2[2] - of1[2]
    for i in range(f):
        if (v + dist) % of2[1] == of2[0]:
            o = v
            break
        v += of1[1]
    return (o, f, of1[2])

ofs = []
for (i, inf) in enumerate(info):
    if inf == 'x':
        v = 1
    else:
        v = int(inf)
    ofs.append((0, v, i))

while len(ofs) > 1:
    ofa = ofs.pop(0)
    ofb = ofs.pop(0)
    ofc = add(ofa, ofb)
    ofs.append(ofc)

print("Result Part 2: ", ofs[0][0] - ofs[0][2])
