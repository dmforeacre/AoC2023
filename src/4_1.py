total = 0
with open("data\\4_1.txt") as f:
    for line in f:
        value = .5
        card, nums = line.split(':')
        myNums, winNums = nums.split('|')
        winNums = list(map(int, winNums.split()))
        for n in list(map(int, myNums.split())):
            if n in winNums:
                value *= 2
        if value >= 1:
            total += value
print(total)