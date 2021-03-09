import regex as re
import os

def checkDataKeys(dataDict : dict):
    reqKey = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    optKey = ['cid']
    valid = True
    for key in reqKey:
        if key not in dataDict:
            return False
    return True

def checkbyr(valueStr):
    pyear = re.compile('(\d{4})')
    m = pyear.match(valueStr)
    if not m:
        return False
    year = int(m.group(1))
    return (year >= 1920 and year <= 2002)

def checkiyr(valueStr):
    pyear = re.compile('(\d{4})')
    m = pyear.match(valueStr)
    if not m:
        return False
    year = int(m.group(1))
    return (year >= 2010 and year <= 2020)

def checkeyr(valueStr):
    pyear = re.compile('(\d{4})')
    m = pyear.match(valueStr)
    if not m:
        return False
    year = int(m.group(1))
    return (year >= 2020 and year <= 2030)

def checkhgt(valueStr):
    phgt = re.compile('(\d*)(\D{2})')
    m = phgt.match(valueStr)
    if not m or len(m.groups()) <= 1:
        return False
    val = int(m.group(1))
    unity = m.group(2)
    if unity == "cm":
        return (val >= 150 and val <= 193)
    elif unity == "in":
        return (val >= 59 and val <= 76)

def checkhcl(valueStr):
    if valueStr[0] != '#':
        return False
    for c in valueStr[1:]:
        asciVal = ord(c)
        if not ((asciVal >=48 and asciVal <= 57) or (asciVal >= 97 and asciVal <= 102)):
            return False
    return True

def checkecl(valueStr):
    validStr = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return valueStr in validStr

def checkpid(valueStr: str):
    ppid = re.compile('(\d*)')
    m = ppid.match(valueStr)
    if not m or len(m.group(1)) > 9 or len(m.group(1)) < 9:
        return False
    return True

def checkDataValues(dataDict : dict):
    reqKey = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    phcl = re.compile('\#(\w{6})')
    byr = dataDict['byr']
    iyr = dataDict['iyr']
    eyr = dataDict['eyr']
    hgt = dataDict['hgt']
    hcl = dataDict['hcl']
    ecl = dataDict['ecl']
    pid = dataDict['pid']
    valid = True
    a = checkbyr(byr)
    b = checkiyr(iyr)
    c = checkeyr(eyr)
    d = checkhgt(hgt)
    e = checkhcl(hcl)
    f = checkecl(ecl)
    g = checkpid(pid)
    """
    print('byr : ', a)
    print('iyr : ', b)
    print('eyr : ', c)
    print('hgt : ', d)
    print('hcl : ', e)
    print('ecl : ', f)
    print('pid : ', g)
    """
    valid = a and b and c and d and e and f and g
    return valid

file = open("input.txt", "r", newline='\n')
p = re.compile('(\D{3})\:(\#?\w*)')


a = file.read()
lines = a.split(2*os.linesep)

validPersons = 0
validPersonsPart1 = 0
for line in lines:
    data = {}
    entries = line.split()
    for entry in entries:
        m = p.match(entry)
        data[m.group(1)] = m.group(2)
    v = checkDataKeys(data)
    if v:
        validPersonsPart1 += 1
        w = checkDataValues(data)
        if w:
            validPersons += 1

print("Part 1 : Number of valid Passports : ", validPersonsPart1)
print("Part 2 : Number of valid Passports : ", validPersons)
