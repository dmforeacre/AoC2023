import math
with open("data\\6_1.txt") as f:
    _, data = f.readline().split(":")
    time = int(''.join(list(data.split())))
    _, data = f.readline().split(":")
    distance = int(''.join(list(data.split())))
    print(time,distance)
    min = math.ceil((time/2)-(math.sqrt(math.pow(time,2)-(4*distance))/2)+.01)
    max = math.ceil((time/2)+(math.sqrt(math.pow(time,2)-(4*distance))/2))
print(max-min)
