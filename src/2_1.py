maxR = 12
maxG = 13
maxB = 14
sum = 0
with open("data\\2_1.txt") as f:
    for line in f:
        game, moves = line.split(":")
        game = list(game.split())[1]
        isPoss = True
        for m in list(moves.split(";")):
            for c in list(m.split(",")):
                num, color = c.split()
                match color:
                    case "red":
                        if int(num) > maxR:
                            isPoss = False
                    case "green":
                        if int(num) > maxG:
                            isPoss = False
                    case "blue":
                        if int(num) > maxB:
                            isPoss = False
        if isPoss:
            sum += int(game)
print(sum)