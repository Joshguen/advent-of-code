import re
f = open("C:\\Users\\Josh\\Documents\\advent of code\\day 4\\input.txt", "r")
total = 0
for x in f:
    cardExclusion = x.split(":", 1)
    grouped = cardExclusion[1].split("|", 1)
    allWinners = re.findall(r'\d+',grouped[0])
    allTicketNumbers = re.findall(r'\d+',grouped[1])
    matches = 0
    for y in allWinners:
        if y in allTicketNumbers:
            matches += 1
    if matches > 0:
        total += 2**(matches-1)
print(total)