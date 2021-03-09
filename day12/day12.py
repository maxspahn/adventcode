import re
from numpy import sin, cos, radians

def F(x, y, t, v):
    return (x+cos(radians(t))*v, y+sin(radians(t))*v, t)

def R(x, y, t, v):
    return (x, y, t-v)

def L(x, y, t, v):
    return (x, y, t+v)

def N(x, y, t, v):
    return (x, y+v, t)

def S(x, y, t, v):
    return (x, y-v, t)

def E(x, y, t, v):
    return (x+v, y, t)

def W(x, y, t, v):
    return (x-v, y, t)

def F2(xs, ys, ts, xw, yw, v):
    for i in range(v):
        xs += xw
        ys += yw
    return (xs, ys, ts, xw, yw)

def R2(xs, ys, ts, xw, yw, v):
    xwn = cos(radians(v)) * xw + sin(radians(v)) * yw
    ywn = -sin(radians(v)) * xw + cos(radians(v)) * yw
    return (xs, ys, ts, xwn, ywn)

def L2(xs, ys, ts, xw, yw, v):
    xwn = cos(-radians(v)) * xw + sin(-radians(v)) * yw
    ywn = -sin(-radians(v)) * xw + cos(-radians(v)) * yw
    return (xs, ys, ts, xwn, ywn)

def N2(xs, ys, ts, xw, yw, v):
    return (xs, ys, ts, xw, yw + v)

def S2(xs, ys, ts, xw, yw, v):
    return (xs, ys, ts, xw, yw - v)

def W2(xs, ys, ts, xw, yw, v):
    return (xs, ys, ts, xw - v, yw)

def E2(xs, ys, ts, xw, yw, v):
    return (xs, ys, ts, xw + v, yw)

def manhattenDist(state):
    return round(abs(state[0]) + abs(state[1]))

funDict = {'F': F, 'N':N, 'R': R, 'L': L, 'W': W, 'E': E, 'S': S}

p = re.compile('(\D)(\d*).*')
file = open('input.txt', 'r')
ins = []
for line in file:
    m = p.match(line)
    ins.append([m.group(1), int(m.group(2))])

s = (0, 0, 0) # x, y, theta (0 =east)
for action in ins:
    s = funDict[action[0]](s[0], s[1], s[2], action[1])
print("Part 1 Result : ", manhattenDist(s))

# Part 2
funDict2 = {'F': F2, 'N':N2, 'R': R2, 'L': L2, 'W': W2, 'E': E2, 'S': S2}
s = (0, 0, 0, 10, 1)
for action in ins:
    s = funDict2[action[0]](s[0], s[1], s[2], s[3], s[4],  action[1])
print("Part 2 Result : ", manhattenDist(s))
