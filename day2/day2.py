import re

file = open("input.txt", "r")
p = re.compile('(\d+)-(\d+)\s(\D):\s(\D+)')

# Part 1
counter = 0
for line in file:
    m = p.match(line)
    minNum = int(m.group(1))
    maxNum = int(m.group(2))
    char = m.group(3)
    password = m.group(4)
    occ = password.count(char)
    if ((occ >= minNum) and (occ <= maxNum)):
        counter += 1

print(counter)

# Part 2
file.seek(0)
counter = 0
for line in file:
    m = p.match(line)
    firstPos = int(m.group(1)) - 1
    secondPos = int(m.group(2)) - 1
    char = m.group(3)
    password = m.group(4)
    firstRight = (password[firstPos] == char)
    secondRight = (password[secondPos] == char)
    if (firstRight or secondRight) and not (firstRight and secondRight):
        counter += 1

print(counter)
