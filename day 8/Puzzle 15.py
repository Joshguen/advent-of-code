import re
f = open("C:\\Users\\Josh\\Documents\\advent of code\\day 8\\input.txt", "r")
directions = f.readline()
directions = directions.split("\n")[0]
f.readline()
index, lefts, rights = ([] for i in range(3))
allSets = [index, lefts, rights]
for x in f:
    map = re.findall(r'[a-zA-Z]{3}', x)
    for y in range(len(allSets)):
        allSets[y].append(map[y])

steps = 0
dCount = 0
current = 0
next = 'AAA'
while steps < 1000000:
    if dCount == len(directions):
        dCount = 0
    current = index.index(next)
    if directions[dCount] == 'L':
        next = lefts[current]
    if directions[dCount] == 'R':
        next = rights[current]
    steps += 1
    dCount += 1
    if next == 'ZZZ':
        break
print (steps)

