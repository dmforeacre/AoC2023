histories = []
with open("data\\9_1.txt") as f:
    for line in f:
        histories.append(list(map(int,line.split())))
totals = []
for h in histories:
    differences = []
    row = []
    for i in range(0, len(h)):
        row.append(h[i])
    differences.append(row)
    index = 0
    isZeros = False
    while not isZeros:
        row = []
        isZeros = True
        for i in range(1, len(differences[index])):
            diff = differences[index][i]-differences[index][i-1]
            row.append(diff)
            if diff != 0:
                isZeros = False
        differences.append(row)
        index += 1
    total = 0
    for d in differences:
        total += d[-1]
    totals.append(total)
print(sum(totals))
