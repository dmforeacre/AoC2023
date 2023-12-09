sum = 0
with open("data\\2_1.txt") as f:
    for line in f:
        game, moves = line.split(":")
        game = list(game.split())[1]
        r = g = b = 0
        for m in list(moves.split(";")):
            for c in list(m.split(",")):
                num, color = c.split()
                match color:
                    case "red":
                        if int(num) > r:
                            r = int(num)
                    case "green":
                        if int(num) > g:
                            g = int(num)
                    case "blue":
                        if int(num) > b:
                            b = int(num)
        sum += r * g * b
print(sum)