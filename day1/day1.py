f = open("input.txt", "r")
values = []
for line in f:
    try:
        values.append(int(line))
    except:
        continue

# two values
isFound = False
for i in values:
    if isFound:
        break;
    for j in values:
        if (i + j) == 2020:
            print(i, j)
            print(i * j)
            isFound = True
            break

# three values
isFound = False
for i in values:
    if isFound:
        break;
    for j in values:
        if isFound:
            break;
        for k in values:
            if (i + j + k) == 2020:
                print(i, j, k)
                print(i * j * k)
                isFound = True
                break
