#with open("data\\8_1.txt") as f:
with open("data/8_1.txt") as f:
    path = f.readline().strip()
    f.readline()
    line = f.readline()
    nodes = {}
    curr = []
    while line:
        key, data = line.split('=')
        l, r = data.strip()[1:-1].split(',')
        nodes[key.strip()] = (l,r.strip())
        if key.strip()[-1] == 'A':
            curr.append(key.strip())
        line = f.readline()
    steps = 0
    pathIndex = 0
    index = 0
    for n in nodes:
        print(index, n, end="")
        currOne = n
        for j in range(0, len(path)):
            if path[j] == 'L':
                currOne = nodes[currOne][0]
            else:
                currOne = nodes[currOne][1]
        print(" ",currOne)
        index += 1
    '''allZ = False
    while not allZ:
        if pathIndex == len(path):
            pathIndex = 0
        for i in range(0, len(curr)):
            if path[pathIndex] == 'L':
                curr[i] = nodes[curr[i]][0]
            else:
                curr[i] = nodes[curr[i]][1]
        steps += 1
        pathIndex += 1
        allZ = True
        for n in curr:
            if n[-1] != 'Z':
                allZ = False
                break'''
print(steps)