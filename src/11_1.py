import math
grid = []
galaxies = []
with open("data\\11_1.txt") as f:
    for line in f:
        row = []
        line = line.strip()
        for c in line:
            row.append(c)
        grid.append(row)
indexes = []
for i in range(len(grid)):
    empty = True
    for c in grid[i]:
        if c == "#":
            empty = False
    if empty:
        indexes.append(i)
for i in range(len(indexes)-1,-1,-1):
    row = "."*len(grid[0])
    grid.insert(indexes[i],row)
indexes.clear()
for i in range(len(grid[0])):
    empty = True
    for j in range(len(grid)):
        if grid[j][i] == "#":
            empty = False
    if empty:
        indexes.append(i)
for i in range(0,len(grid)):    
    newStr = ""
    for j in range(0,len(grid[i])):
        newStr += grid[i][j]
        if j in indexes:
            newStr += "."
    grid[i] = newStr
for i in range(0,len(grid)):
    for j in range(0,len(grid[i])):
        if grid[i][j] == "#":
            galaxies.append((i,j))
sum = 0
for i in range(0,len(galaxies)):
    for j in range(i+1,len(galaxies)):
        dist = abs(galaxies[j][0]-galaxies[i][0]) + abs(galaxies[j][1]-galaxies[i][1])
        sum += dist
print(sum)