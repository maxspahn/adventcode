import re
from pprint import pprint

def solveExp(mathList):
    a = int(mathList.pop(0))
    ope = mathList.pop(0)
    b = int(mathList.pop(0))
    if ope == '+':
        mathList.insert(0, str(a + b))
    elif ope == '*':
        mathList.insert(0, str(a * b))

def solveSimpleExp(mathExp):
    mathList = mathExp.split()
    while len(mathList) > 1:
        solveExp(mathList)
    return mathList[0]

def evalExpPart2(exp):
    print(exp)
    p1 = re.compile('[\(\)]')
    p2 = re.compile('(.*)\((.*?)\)(.*)')
    p3 = re.compile('(.*?)(\d*\s\+\s\d*)(.*)')
    if '(' not in exp and ')' not in exp and '+' not in exp:
        res = solveSimpleExp(exp)
    elif '(' not in exp and ')' not in exp:
        m3 = p3.match(exp)
        """
        for i in range(len(m3.groups())):
            print(m3.group(i))
        """
        if (len(m3.groups()) == 2):
            newExp = m3.group(1) + str(solveSimpleExp(m3.group(2)))
        elif (len(m3.groups()) == 3):
            newExp = m3.group(1) + str(solveSimpleExp(m3.group(2))) + m3.group(3)
        res = evalExpPart2(newExp)
    else:
        m2 = p2.match(exp)
        if (len(m2.groups()) == 2):
            newExp = m2.group(1) + evalExpPart2(m2.group(2))
        elif (len(m2.groups()) == 3):
            newExp = m2.group(1) + evalExpPart2(m2.group(2)) + m2.group(3)
        res = evalExpPart2(newExp)
    return res

def evalExp(exp):
    print(exp)
    p1 = re.compile('[\(\)]')
    p2 = re.compile('(.*)\((.*?)\)(.*)')
    if '(' not in exp and ')' not in exp:
        res = solveSimpleExp(exp)
    else:
        m2 = p2.match(exp)
        if (len(m2.groups()) == 2):
            newExp = m2.group(1) + evalExp(m2.group(2))
        elif (len(m2.groups()) == 3):
            newExp = m2.group(1) + evalExp(m2.group(2)) + m2.group(3)
        res = evalExp(newExp)
    return res

def cleaningLines(file):
    cleanLines = []
    tempLine = ""
    started = False
    for line in file:
        if line[0] == '+' or line[0] == '*':
            cleanLines[-1] += " " + line[:-1]
        elif line[-2] == '*' or line[-2] == '+':
            cleanLines.append(line[:-1])
            started = True
        elif started == True:
            cleanLines[-1] += " " + line[:-1]
            started = False
        else:
            cleanLines.append(line[:-1])
    return cleanLines

file = open('inputSmall.txt', 'r')
file = open('inputTest.txt', 'r')
file = open('input.txt', 'r')

cleanLines = cleaningLines(file)

s = 0
for line in cleanLines:
    print("----")
    print(line)
    r = evalExp(line)
    print(r)
    s += int(r)

print("Part 1 Result : ", s)

s = 0
for line in cleanLines:
    print("----")
    print(line)
    r = evalExpPart2(line)
    print(r)
    s += int(r)

print("Part 2 Result : ", s)
