import math
maps = []
for i in range(0, 7):
    maps.append([])

def fillMap(f, curMap):
    line = f.readline()
    while line and line != "\n":
        curMap.append(list(map(int, line.split())))
        line = f.readline()

with open("data\\5_1test.txt") as f:
    l, r = f.readline().split(":")
    seeds = list(map(int, r.split()))
    f.readline()
    f.readline()
    for i in range(0, 7):
        fillMap(f, maps[i])
        f.readline()
    '''min = math.inf
    for i in range(0, int(len(seeds)/2 + 1), 2):
        for j in range(seeds[i], seeds[i] + seeds[i + 1]):
            val = j
            for m in range(0, 7):
                isMapped = False
                for n in range(0, len(maps[m])):
                    if not isMapped and val >= maps[m][n][1] and val <= maps[m][n][1] + maps[m][n][2]:
                        isMapped = True
                        val = maps[m][n][0] + (val - maps[m][n][1])
                #if not isMapped:

            if val < min:
                min = val'''
    min = math.inf
    for i in range(0, len(maps[6])):
        curr = maps[6][i]
        if curr[1] < min:
            min = curr[1]
            index = i

print(min, i)