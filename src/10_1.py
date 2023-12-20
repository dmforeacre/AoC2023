def FindPath(grid, pipe, prev, p):
    match pipe:
        case "S":
            if prev != (0,0):
                return "Done"
            if p[0]-1 > 0 and (grid[p[0]-1][p[1]] == "|" or grid[p[0]-1][p[1]] == "F" or grid[p[0]-1][p[1]] == "7"):
                return (p[0]-1,p[1])
            if p[0]+1 < len(grid)-1 and (grid[p[0]+1][p[1]] == "|" or grid[p[0]+1][p[1]] == "L" or grid[p[0]+1][p[1]] == "J"):
                return (p[0]+1,p[1])
            if p[1]-1 > 0 and (grid[p[0]][p[1]-1] == "-" or grid[p[0]][p[1]-1] == "F" or grid[p[0]][p[1]-1] == "L"):
                return (p[0],p[1]-1)
            if p[1]+1 > 0 and (grid[p[0]][p[1]+1] == "-" or grid[p[0]][p[1]+1] == "J" or grid[p[0]][p[1]+1] == "7"):
                return (p[0],p[1]+1)
        case "-":
            if prev == (p[0],p[1]-1):
                return (p[0],p[1]+1)
            else:
                return (p[0],p[1]-1)
        case "|":
            if prev == (p[0]-1,p[1]):
                return (p[0]+1,p[1])
            else:
                return (p[0]-1,p[1])
        case "L":
            if prev == (p[0]-1,p[1]):
                return (p[0],p[1]+1)
            else:
                return (p[0]-1,p[1])
        case "F":
            if prev == (p[0],p[1]+1):
                return (p[0]+1,p[1])
            else:
                return (p[0],p[1]+1)
        case "J":
            if prev == (p[0]-1,p[1]):
                return (p[0],p[1]-1)
            else:
                return (p[0]-1,p[1])
        case "7":
            if prev == (p[0],p[1]-1):
                return (p[0]+1,p[1])
            else:
                return (p[0],p[1]-1)
            
grid = []
sLoc = (0,0)
with open("data\\10_1.txt") as f:
    rowNum = 0
    for line in f:
        row = []
        colNum = 0
        for c in line.strip():
            if c == 'S':
                sLoc = (rowNum, colNum)
            row.append(c)
            colNum += 1
        grid.append(row)
        rowNum += 1
path = []
prevNode = sLoc
currNode = FindPath(grid, "S", (0,0), sLoc)
while currNode != sLoc:
    path.append(currNode)
    tempNode = prevNode
    prevNode = currNode
    currNode = FindPath(grid, grid[prevNode[0]][prevNode[1]],tempNode, prevNode)
print(round(len(path)/2))