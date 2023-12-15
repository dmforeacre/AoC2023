#with open("data\\8_1.txt") as f:
with open("data/8_1.txt") as f:
    path = f.readline().strip()
    f.readline()
    line = f.readline()
    nodes = {}
    while line:
        key, data = line.split('=')
        l, r = data.strip()[1:-1].split(',')
        nodes[key.strip()] = (l,r.strip())
        line = f.readline()
    curr = 'AAA'
    steps = 0
    while curr != 'ZZZ':
        for i in range(0, len(path)):
            if curr == 'ZZZ':break
            if path[i] == 'L':
                curr = nodes[curr][0]
            else:
                curr = nodes[curr][1]
            steps += 1
print(steps)