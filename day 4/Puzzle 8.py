import re
f = open("C:\\Users\\Josh\\Documents\\advent of code\\day 4\\input.txt", "r")
ticketAmounts = [1] * 205
total = 0
xCount = 0
for x in f:
    cardExclusion = x.split(":", 1)
    grouped = cardExclusion[1].split("|", 1)
    allWinners = re.findall(r'\d+',grouped[0])
    allTicketNumbers = re.findall(r'\d+',grouped[1])
    ticketAdder = 1
    for y in allWinners:
        if y in allTicketNumbers:
            ticketAmounts[xCount + ticketAdder] += ticketAmounts[xCount]
            ticketAdder += 1
    total += ticketAmounts[xCount]
    xCount += 1
print(total)