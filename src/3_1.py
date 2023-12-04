grid = []
with open("src\\3_1.txt") as f:
    for line in f:
        row = []
        for c in line:
            row.append(c)
        grid.append(row)
for j in range(0, len(grid)):
    for i in range(0, len(grid[0])):
        print(grid[i][j])