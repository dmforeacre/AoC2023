sum = 0
digits = {("one", "1"), ("two", "2"), ("three", "3"), ("four", "4"), ("five", "5"), ("six", "6"), ("seven", "7"), ("eight", "8"), ("nine", "9"), ("zero", "0")}
with open("data\\1_1.txt") as f:
    for line in f:
        findex = 0
        lindex = len(line) - 1
        while not line[findex].isnumeric():
            findex += 1
        first = line[findex]
        while not line[lindex].isnumeric():
            lindex -= 1
        last = line[lindex]
        for d in digits:
            i = line.find(d[0])
            if i == -1: continue
            if i < findex:
                findex = i
                first = d[1]
            i = line.rfind(d[0])
            if i > lindex:
                lindex = i
                last = d[1]
        sum += int(first + last)
print(sum)