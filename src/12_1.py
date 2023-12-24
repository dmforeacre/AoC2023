springs = []
counts = []
with open("data\\12_1test.txt") as f:
    for line in f:
        s, c = line.split()
        springs.append(s.strip())
        counts.append(c.strip())
for i in range(0,len(springs)):
    index = 0
    for n in counts[i]:
        while index < len(springs[i]):
            if springs[i][index] == "#":
                break
            index += 1