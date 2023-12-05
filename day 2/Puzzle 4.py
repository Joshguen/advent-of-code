import re
f = open("C:\\Users\\Josh\\Documents\\advent of code\\day 2\\input.txt", "r")
total = 0
gameCount = 0
for x in f:
  count = 0
  redMax = 0
  blueMax = 0
  greenMax = 0
  for match in re.finditer(r'\d+', x):
    count += 1
    #ignore first match since it's the game count
    if (count != 1):
      if (x[match.end() + 1] == 'r' and int(match.group()) > redMax):
        redMax = int(match.group())
      if (x[match.end() + 1] == 'g' and int(match.group()) > blueMax):
        blueMax = int(match.group())
      if (x[match.end() + 1] == 'b' and int(match.group()) > greenMax):
        greenMax = int(match.group())
  total += redMax * blueMax * greenMax
print(total)