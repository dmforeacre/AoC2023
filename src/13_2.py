def getNumDif(grid, i):
    count = 0
    numDiff = 0
    while i-1-count >= 0 and i+count < len(grid):
        for n in range(0,len(grid[i])):
            if grid[i-1-count][n] != grid[i+count][n]:
                numDiff += 1
                if numDiff >= 2:
                    return numDiff
        count += 1
    return numDiff

grids = []
with open("data\\13_1.txt") as f:
    line = f.readline()
    while line:
        grid = []
        while line and line != "\n":
            grid.append(line.strip())
            line = f.readline()
        grids.append(grid)
        line = f.readline()
total = 0
c = 0
for grid in grids:
    c += 1
    refFound = False
    for i in range(1, len(grid)):
        if getNumDif(grid, i) == 1:
            refFound = True
            total += 100 * i
            break
    if not refFound:
        transGrid = []
        for i in range(0, len(grid[0])):
            newRow = ""
            for row in grid:
                newRow += row[i]
            transGrid.append(newRow)
        for i in range(1, len(transGrid)):
            if getNumDif(transGrid, i) == 1:
                total += i
                break
print(total)