sum = 0
with open("src\\1_1.txt") as f:
    for line in f:
        index = 0
        while not line[index].isnumeric():
            index += 1
        first = line[index]
        index = len(line) - 1
        while not line[index].isnumeric():
            index -= 1
        last = line[index]
        sum += int(first + last)
print(sum)