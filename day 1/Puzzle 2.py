import re
f = open("C:\\Users\\Josh\\Documents\\advent of code\\puzzle 1\\input.txt", "r")
total = 0
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for x in f:
  lowestIndex = 100
  lowestValue = 100
  highestIndex = -1
  highestValue = -1

  for i in numbers:
    res = [k for k in range(len(x)) if x.startswith(str(i), k)]
    if (res.__len__() > 0):
      for l in range(len(res)):
        if (res[l] < lowestIndex):
          lowestIndex = res[l]
          lowestValue = x[res[l]]
        if (res[l] > highestIndex):
          highestIndex = res[l]
          highestValue = x[res[l]]
  for j in range(words.__len__()):
    res = [k for k in range(len(x)) if x.startswith(words[j], k)]
    foundindex = x.find(words[j])
    if (res.__len__() > 0):
      for l in range(len(res)):
        if (res[l] < lowestIndex):
            lowestIndex = res[l]
            lowestValue = j+1
        if (res[l] > highestIndex):
            highestIndex = res[l]
            highestValue = j+1
        
  current = str(lowestValue)+str(highestValue)
  total += int(current)
print(total)
