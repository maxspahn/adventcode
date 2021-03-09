from tree import OptionString
import re


file = open("input.txt", 'r')
file = open("inputTest.txt", 'r')

pRule = re.compile('(\d+)\:\s"?([^"]*)"?')
pText = re.compile('(\D+).*')

rules = {}
messages = []
opStrs = {}
opStr = OptionString(0)
for line in file:
    mRule = pRule.match(line[:-1])
    mText = pText.match(line[:-1]) 
    if mRule:
        for i, split in enumerate(re.split('\s\|\s', mRule.group(2))):
            options = [[val] for val in split.split()]
            if i == 0:
                opStr = OptionString(index = int(mRule.group(1)), options=options)
            else:
                opStr.appendOption(options)
        opStrs[mRule.group(1)] = opStr
    if mText:
        messages.append(mText.group(1))

for o in opStrs.keys():
    print(o)
    print(opStrs[o])

print(opStrs['0'])
for i in range(opStrs['0'].len()):
    val = opStrs['0'].getOptions(i)
    print(val[0])

