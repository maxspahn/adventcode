import re
from pprint import pprint


def processRule(index, rules):
    allNewOptions = []
    for option in rules[index]:
        newOptions = []
        for c in option.split():
            if c == "31" and anyOptionContainsNumber(rules["31"]):
                if not newOptions:
                    newOptions.append(c)
                else:
                    for i in range(len(newOptions)):
                        newOptions[i] += " " + c
                continue
            if c == "42" and anyOptionContainsNumber(rules["42"]):
                if not newOptions:
                    newOptions.append(c)
                else:
                    for i in range(len(newOptions)):
                        newOptions[i] += " " + c
                continue
            if c == 'a' or c == 'b' or 'a' in c or 'b' in c:
                if not newOptions:
                    newOptions.append(c)
                else:
                    for i in range(len(newOptions)):
                        newOptions[i] += " " + c
                continue
            else:
                if not newOptions:
                    for subRule in rules[c]:
                        newOptions.append(subRule)
                else:
                    temp = []
                    for opt in newOptions:
                        for subRule in rules[c]:
                            temp.append(opt + " " + subRule)
                    newOptions = temp
        allNewOptions += newOptions
        strippedOptions = stripOptions(allNewOptions)
        if index == "42":
            strippedOptions = addLoop(strippedOptions)
        if index == "31":
            strippedOptions = addLoop(strippedOptions)
        rules[index] = strippedOptions

def addInnerLoop(options, j):
    if not anyOptionContainsNumber(options):
        for i in range(len(options)):
            if re.match('.*\(.*', options[i]):
                continue
            options[i] = "(" + options[i][0:j] + ")*(" + options[i][j:] + ")*"
    return options


def addLoop(options):
    if not anyOptionContainsNumber(options):
        for i in range(len(options)):
            if re.match('.*\(.*', options[i]):
                continue
            options[i] = "(" + options[i] + ")*"
    return options

def stripOptions(options):
    if not anyOptionContainsNumber(options):
        for i in range(len(options)):
            options[i] = options[i].replace(" ", "")
    return options

def anyOptionContainsNumber(options):
    for option in options:
        if re.match('.*\d.*', option):
            return True
    return False

def anyOptionContainsLoop(options):
    for option in options:
        if re.match('.*\(.*', option):
            return True
    return False

def processRules(rules):
    for i in range(5):
        print("sorting run : ", i)
        print(len(rules["0"]))
        for key in rules.keys():
            if anyOptionContainsNumber(rules[key]):
                processRule(key, rules)
    for key in rules.keys():
        for i in range(len(rules[key])):
            rules[key][i] = rules[key][i].replace(" ", "")

def checkRuleZero(message, rule):
    for r in rule:
        p = re.compile(r + "$")
        m = p.match(message)
        if m:
            print(message)
            print(r)
            print(m)
            return True
    return False

file = open("inputTest.txt", 'r')
file = open("inputNoLoop.txt", 'r')

pRule = re.compile('(\d+)\:\s"?([^"]*)"?')
pText = re.compile('(\D+).*')

rules = {}
messages = []
for line in file:
    mRule = pRule.match(line[:-1])
    mText = pText.match(line)
    if mRule:
        rules[mRule.group(1)] = re.split('\|', mRule.group(2))
    if mText:
        messages.append(mText.group(1)[:-1])

processRules(rules)
"""
pprint(rules["8"])
pprint(rules["11"])
pprint("42")
pprint(rules["42"])
pprint("13")
pprint(rules["13"])
pprint("8")
pprint(rules["8"])
pprint("11")
pprint(rules["11"])
"""
pprint(rules["0"])


# Check rules
counter = 0
for msg in messages:
    if checkRuleZero(msg, rules["0"]):
        counter += 1
print("Part 1 Result : ", counter)


