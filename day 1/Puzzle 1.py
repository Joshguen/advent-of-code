import re
f = open("C:\\Users\\Josh\\Documents\\advent of code\\day 1\\input.txt", "r")
total = 0

for x in f:
  first = re.search(r'\d', x)[0]
  all = re.findall(r'\d',x)
  a = all.__len__()
  last = all[a-1]
  current = first+last
  total += int(current)
print (total)