from dataclasses import dataclass
import operator

@dataclass
class CamelHand:
    hand: list
    bid: int

f = open("C:\\Users\\Josh\\Documents\\advent of code\\day 7\\input.txt", "r")

highList, pairList, twoPairList, threeList, fullHList, fourList, fiveList = ([] for i in range(7))
allList = [highList, pairList, twoPairList, threeList, fullHList, fourList, fiveList]
for x in f:
    input = x.split(" ", 1)
    found1, found2, found3, found4 = ([] for i in range(4))
    allFound = [found1, found2, found3, found4]
    adjusted = []
    for i in input[0]:
        current = i
        if current.isalpha:
            match current:
                case 'T':
                    current = 10
                case 'J':
                    current = 11
                case 'Q':
                    current = 12
                case 'K':
                    current = 13
                case 'A':
                    current = 14
        adjusted.append(int(current))
        for y in allFound:
            if current in y:
                y.append(current)
                break
            elif len(y) == 0:
                y.append(current)
                break
    largest = 0
    largestIndex = -1
    second = 0
    for y in range(len(allFound)):
        if len(allFound[y]) >= largest:
            largest = len(allFound[y])
            largestIndex = y
    for y in range(len(allFound)):
        if len(allFound[y]) >= second and not y == largestIndex:
            second = len(allFound[y])

    cHand = CamelHand(adjusted, int(input[1]))
    match largest:
        case 1:
            highList.append(cHand)
        case 2:
            if second == 2:
                twoPairList.append(cHand)
            else:
                pairList.append(cHand)
        case 3:
            if second == 2:
                fullHList.append(cHand)
            else:
                threeList.append(cHand)
        case 4:
            fourList.append(cHand)
        case 5:
            fiveList.append(cHand)
previous = 0
winnings = 0
for x in allList:
    x.sort(key=operator.attrgetter('hand'))
    for y in range(len(x)):
        winnings += x[y].bid * (y + 1 + previous)
    previous += len(x)
print(winnings)
