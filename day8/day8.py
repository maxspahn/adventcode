import re

def performAction(v, c, action):
    if action[0] == 'acc':
        v += action[1]
        c += 1
    elif action[0] == 'nop':
        c += 1
    elif action[0] == 'jmp':
        c += action[1]
    return (c, v)

# Parse input file
file = open('input.txt', 'r');
p = re.compile('(\D{3})\s(\-?\+?\d*)')
actionList = []
for line in file:
    m = p.match(line);
    actionList.append([m.group(1), int(m.group(2))])

# set runtime variables
visited = [0,] * len(actionList)
curLine = 0
value = 0
# Run one instance
while visited[curLine] == 0:
    visited[curLine] = 1
    (curLine, value) = performAction(value, curLine, actionList[curLine])
print("Result Part 1: ", value)

# Part 2
cIndex = 0
termin = 0
while termin == 0:
    # Search for next line that can be modified
    while actionList[cIndex][0] == 'acc':
        cIndex += 1
    # do modification
    if actionList[cIndex][0] == 'jmp':
        actionList[cIndex][0] = 'nop'
    elif actionList[cIndex][0] == 'nop':
        actionList[cIndex][0] = 'jmp'
    # Reset values 
    visited = [0,] * len(actionList)
    curLine = 0
    value = 0
    # Play one instance
    while curLine < len(visited) and visited[curLine] == 0 :
        visited[curLine] = 1
        (curLine, value) = performAction(value, curLine, actionList[curLine])
    termin = visited[-1]
    # undo modification
    if actionList[cIndex][0] == 'jmp':
        actionList[cIndex][0] = 'nop'
    elif actionList[cIndex][0] == 'nop':
        actionList[cIndex][0] = 'jmp'
    cIndex += 1

print('Part 2: bug in line : ', cIndex - 1, ', final accumlator value : ', value)
