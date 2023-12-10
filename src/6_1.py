import math
with open("data\\6_1.txt") as f:
    _, data = f.readline().split(":")
    times = list(map(int, data.split()))
    _, data = f.readline().split(":")
    distances = list(map(int, data.split()))
product = 1
for i in range(0,len(times)):
    min = math.ceil((times[i]/2)-(math.sqrt(math.pow(times[i],2)-(4*distances[i]))/2)+.01)
    max = math.ceil((times[i]/2)+(math.sqrt(math.pow(times[i],2)-(4*distances[i]))/2))
    product *= max - min
    print(min, max, max-min)
print(product)
