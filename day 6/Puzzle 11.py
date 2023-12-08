import re
f = open("C:\\Users\\Josh\\Documents\\advent of code\\day 6\\input.txt", "r")

times = re.findall(r'\d+',f.readline())
distances = re.findall(r'\d+',f.readline())
total = 1
for i in range (len(times)):
    waysToWin = 0
    for j in range(int(times[i])):
        if j * (int(times[i])-j) > int(distances[i]):
            waysToWin += 1
    total *= waysToWin
print(total)