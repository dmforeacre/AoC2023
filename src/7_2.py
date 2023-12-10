def getCardValue(c):
    if c.isnumeric():
        val = int(c)
    else:
        match(c):
            case 'T': val = 10
            case 'Q': val = 12
            case 'K': val = 13
            case 'A': val = 14
            case 'J': val = 1
    return val

def getHandValue(cards):
    counts = dict((i, cards.count(i)) for i in cards)
    if 'J' in cards:
        num = 0
        card = ''
        for c in counts:
            if counts[c] > num and c != 'J':
                num = counts[c]
                card = c
        newCards = cards.replace('J', card)
        counts = dict((i, newCards.count(i)) for i in newCards)
    rank1 = 0
    rank2 = 0
    card = ''
    for c in counts:
        if counts[c] >= rank1 and c != card:
            rank2 = rank1
            rank1 = counts[c]
            card = c
        elif rank2 == 0 and c != card:
            rank2 = counts[c]
    value = 7
    match(rank1):
        case 5: value = 7
        case 4: value = 6
        case 3: 
            if rank2 == 2:
                value = 5
            else:
                value = 4
        case 2:
            if rank2 == 2:
                value = 3
            else:
                value = 2
        case 1:
            value = 1
    return value

def lessThan(left, right):
    lVal = getHandValue(left)
    rVal = getHandValue(right)
    if lVal < rVal:
        return True
    elif lVal == rVal:
        for i in range(0, len(left)):
            if getCardValue(left[i]) < getCardValue(right[i]):
                return True
            elif getCardValue(left[i]) > getCardValue(right[i]):
                return False
    return False

hands = []
with open("data\\7_1.txt") as f:
    for line in f:
        cards, bet = line.split()
        hands.append((cards, bet))
sortedHands = []
for hand in hands:
    if len(sortedHands) == 0:
        sortedHands.append(hand)
    else:
        i = 0
        while i < len(sortedHands) and lessThan(sortedHands[i][0], hand[0]):
            i += 1
        sortedHands.insert(i, hand)
sum = 0
for i in range(0,len(sortedHands)):
    sum += (i + 1) * int(sortedHands[i][1])
print(sum)