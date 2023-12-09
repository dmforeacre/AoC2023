with open("data\\5_1.txt") as f:
    l, r = f.readline().split(":")
    seeds = list(map(int, r.split()))
    f.readline()
    f.readline()
    line = f.readline()
    while line:
        print("Next Category")
        maps = []
        while line and line != "\n":
            maps.append(list(map(int, line.split())))
            line = f.readline()
        for i in range(0, len(seeds)):
            isMapped = False
            for m in maps:
                if not isMapped and seeds[i] >= m[1] and seeds[i] <= m[1] + m[2]:
                    isMapped = True
                    print(seeds[i], "->", m[0] + (seeds[i] - m[1]))
                    seeds[i] = m[0] + (seeds[i] - m[1])
            if not isMapped:
                print(seeds[i], "->", seeds[i], ": not mapped")
        f.readline()
        line = f.readline()
print(min(seeds))