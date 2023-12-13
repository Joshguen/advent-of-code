import re
f = open("C:\\Users\\Josh\\Documents\\advent of code\\day 8\\input.txt", "r")
directions = f.readline()
directions = directions.split("\n")[0]
f.readline()
index, lefts, rights = ([] for i in range(3))
allSets = [index, lefts, rights]
for x in f:
    map = re.findall(r'[a-zA-Z0-9]{3}', x)
    for y in range(len(allSets)):
        allSets[y].append(map[y])
allStarts = []
allEnds = []
for i in index:
    if i[2] == 'A':
        allStarts.append(i)
for i in range (len(allStarts)):
    steps = 0
    dCount = 0
    current = 0
    while steps < 1000000:
        if dCount == len(directions):
            dCount = 0
        current = index.index(allStarts[i])
        if directions[dCount] == 'L':
            allStarts[i] = lefts[current]
        if directions[dCount] == 'R':
            allStarts[i] = rights[current]
        steps += 1
        dCount += 1
        if allStarts[i][2] == 'Z':
            allEnds.append(steps)
            break
#prints a list of First instance of each Z
#plugging these into a LCM multiplier returns the answer
print (allEnds)
