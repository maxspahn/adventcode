import re

def checkVal(val, cla):
    return val in cla[1]

def checkTicket(values, classes):
    inValids = []
    for val in values:
        valid = False
        for cla in classes:
            valid = checkVal(val, cla)
            if valid:
                break
        if not valid:
            inValids.append(val)
    return inValids

def checkTicketPart2(values, classes):
    inValids = []
    notValDict ={}
    validDict = {}
    for (i, val) in enumerate(values):
        validDict[i] = []
        notValDict[i] = []
        valid = False
        for cla in classes:
            if checkVal(val, cla):
                valid = True
                validDict[i].append(cla[0])
            else:
                notValDict[i].append(cla[0])
        if not valid:
            inValids.append(val)
    return (inValids, validDict, notValDict)

def processClaString(claStr):
    validVal = []
    groups = claStr.split(' or ')
    for group in groups:
        minMax = [int(val) for val in group.split('-')]
        validVal += list(range(minMax[0], minMax[1]+1))
    return validVal

file = open('input.txt', 'r')

pCla = re.compile('(\D*)\:\s(\d*\-\d*.*)')
pHea = re.compile('.*ticket.*')
pTic = re.compile('.*\,.*')

classes = []
section = 0
totInvalids = []

for line in file:
    mCla = pCla.match(line)
    if mCla:
        claName = mCla.group(1)
        vv = processClaString(mCla.group(2))
        classes.append((claName, vv))
    mHea = pHea.match(line)
    if mHea:
        section += 1
    mTic = pTic.match(line)
    if mTic and section == 2:
        val = [int(i) for i in line.split(',')]
        totInvalids += checkTicket(val, classes)

print("Part 1 Result : ", sum(totInvalids))

file.seek(0)
section = 0
indexCand = {}
indexNotCand = {0:[], 1:[], 2:[]}
classes = []

for line in file:
    mCla = pCla.match(line)
    if mCla:
        claName = mCla.group(1)
        vv = processClaString(mCla.group(2))
        classes.append((claName, vv))
        indexCand[claName] = []
    mHea = pHea.match(line)
    if mHea:
        section += 1
    mTic = pTic.match(line)
    if mTic and section == 1:
        myTicket = [int(i) for i in line.split(',')]
    if mTic and section == 2:
        val = [int(i) for i in line.split(',')]
        (invalids, validDict, notValidDict) = checkTicketPart2(val, classes)
        if not invalids:
            for key in notValidDict.keys():
                if key in indexNotCand.keys():
                    for val in notValidDict[key]:
                        if val not in indexNotCand[key]:
                            indexNotCand[key].append(val)
                else:
                    indexNotCand[key] = notValidDict[key]
            for key in validDict.keys():
                for val in validDict[key]:
                    if key not in indexCand[val]:
                        indexCand[val].append(key)

# Clean indexCand
for key in indexNotCand.keys():
    for val in indexNotCand[key]:
        indexCand[val].remove(key)
fieldsMapping = {}
#for i in range(1):
while len(fieldsMapping) < len(indexCand.keys()):
    for key in indexCand.keys():
        choices = indexCand[key]
        validChoices = []
        for choice in choices:
            if choice not in fieldsMapping.keys():
                validChoices.append(choice)
        if len(validChoices) == 1:
            fieldsMapping[validChoices[0]] = key


pDep = re.compile('.*departure.*')
s = 1
for key in fieldsMapping.keys():
    if pDep.match(fieldsMapping[key]):
        s *= myTicket[key]

print("Part 2 Result : ", s)
