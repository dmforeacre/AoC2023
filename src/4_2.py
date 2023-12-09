total = 0
cardNum = 0
cards = [1] * 202
with open("data\\4_1.txt") as f:
    for line in f:
        card, nums = line.split(':')
        myNums, winNums = nums.split('|')
        winNums = list(map(int, winNums.split()))
        winners = 0
        for n in list(map(int, myNums.split())):
            if n in winNums:
                winners += 1
        print(winners)
        for n in range(0, cards[cardNum]):
            if winners > 0:
                for i in range(0, winners):
                    cards[cardNum + i + 1] += 1        
        cardNum += 1
print(sum(cards))