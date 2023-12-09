import re

def isSymbol(grid, x, y):
    if grid[x][y].isnumeric() or grid[x][y] == '.':
        return False
    return True

regex = re.compile(r'(\D*)(\d*)')
nums = []
grid = []
sum = 0
with open("data\\3_1.txt") as f:
#with open("data/3_1test.txt") as f:
    for line in f:
        rowNums = []
        match = re.findall(regex, line)
        for m in match:
            if m[1] != "":
                rowNums.append(m[1])
        grid.append(line)
        nums.append(rowNums)
for i in range(0, len(grid)):
    index = 0
    for num in nums[i]:
        isPart = False
        index = grid[i].find(num, index)
        if i > 0:    
            if index - 1 > 0:
                if not isPart and isSymbol(grid, i - 1, index - 1):
                    print(num,end=" ")
                    #print(num, "is a valid part, upper left")
                    isPart = True
            for j in range(index, index + len(num)):
                if not isPart and isSymbol(grid, i - 1, j):
                    print(num,end=" ")
                    #print(num, "is a valid part, top",j)
                    isPart = True
            if index + len(num) + 1 < len(grid[i]):
                if not isPart and isSymbol(grid, i - 1, index + len(num)):
                    print(num,end=" ")
                    #print(num, "is a valid part, upper right")
                    isPart = True
        if index > 0:
            if not isPart and isSymbol(grid, i, index - 1):
                print(num,end=" ")
                #print(num, "is valid part, left")
                isPart = True
        if index + len(num) + 1 < len(grid[i]):
            if not isPart and isSymbol(grid, i, index + len(num)):
                print(num,end=" ")
                #print(num, "is valid part, right")
                isPart = True
        if i < len(grid) - 1:
            if index - 1 > 0:
                if not isPart and isSymbol(grid, i + 1, index - 1):
                    print(num,end=" ")
                    #print(num, "is a valid part, lower left")
                    isPart = True
            for j in range(index, index + len(num)):
                if not isPart and isSymbol(grid, i + 1, j):
                    print(num,end=" ")
                    #print(num, "is a valid part, bot",j)
                    isPart = True
            if index + len(num) + 1 < len(grid[i]):
                if not isPart and isSymbol(grid, i + 1, index + len(num)):
                    print(num,end=" ")
                    #print(num, "is a valid part, lower right")
                    isPart = True
        if isPart:
            sum += int(num)
print(sum)