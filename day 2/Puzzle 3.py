import re
f = open("C:\\Users\\Josh\\Documents\\advent of code\\day 2\\input.txt", "r")
total = 0
gameCount = 0
for x in f:
  count = 0
  flag = 0
  for match in re.finditer(r'\d+', x):
    count += 1
    #ignore first match since it's the game count
    if (count == 1):
      gameCount+=1
    else:
      if (x[match.end() + 1] == 'r' and int(match.group()) > 12):
        flag = 1
      if (x[match.end() + 1] == 'g' and int(match.group()) > 13):
        flag = 1
      if (x[match.end() + 1] == 'b' and int(match.group()) > 14):
        flag = 1
  if (flag == 0):
    total += gameCount
print(total)