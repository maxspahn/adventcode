import os
import re
f = open("input.txt", 'r')

p = re.compile('(\d*)\s(.*)\sbags?')

fullDict = {}
invDict = {}
text = re.split('\.\n', f.read())
for line in text[:-1]:
    infos = line.replace('\n', ' ').split(' bags contain ')
    key = infos[0]
    valspl = infos[1].split(', ')
    vallist = []
    for valSin in valspl:
        m = p.match(valSin)
        if m:
            vallist.append([m.group(2) , int(m.group(1))])
            if m.group(2) in invDict.keys():
                invDict[m.group(2)].append(key)
            else:
                invDict[m.group(2)] = [key]
    fullDict[key] = vallist

print("finished parsing")

toCheck = ['shiny gold']
alreadyChecked = ['shiny gold']

counter = 0
while toCheck:
    key = toCheck.pop()
    if key not in alreadyChecked:
        counter += 1
    alreadyChecked.append(key)
    if key in invDict.keys():
        toCheck += invDict[key]

print("Result Part 1 :", counter)

## Print 2
toCheck = [['shiny gold', 1]]
nbBags = -1 # account for non counting shiny gold bag

while toCheck:
    key = toCheck.pop()
    val = fullDict[key[0]]
    multi = key[1]
    nbBags += key[1]
    for itemPair in val:
        item = itemPair[0]
        nb = itemPair[1]
        toCheck.append([item, multi * nb])

print("Result Part 2 :", nbBags)



