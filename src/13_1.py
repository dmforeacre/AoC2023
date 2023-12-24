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
for grid in grids:
    refFound = False
    for i in range(1, len(grid)):
        if grid[i-1] == grid[i]:
            count = 1
            reflection = True
            while i-1-count >= 0 and i+count < len(grid):
                if grid[i-1-count] != grid[i+count]:
                    reflection = False
                count += 1
            if reflection:
                refFound = True
                total += 100 * i
    if not refFound:
        transGrid = []
        for i in range(0, len(grid[0])):
            newRow = ""
            for row in grid:
                newRow += row[i]
            transGrid.append(newRow)
        for i in range(1, len(transGrid)):
            if transGrid[i-1] == transGrid[i]:
                count = 1
                reflection = True
                while i-1-count >= 0 and i+count < len(transGrid):
                    if transGrid[i-1-count] != transGrid[i+count]:
                        reflection = False
                    count += 1
                if reflection:
                    refFound = True
                    total += i            
print(total)