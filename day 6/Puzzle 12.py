import re
f = open("C:\\Users\\Josh\\Documents\\advent of code\\day 6\\input.txt", "r")

times = re.findall(r'\d+',f.readline())
distances = re.findall(r'\d+',f.readline())
time = ""
time = ""
for x in times:
    time = time + x
distance = ""
for x in distances:
    distance = distance + x

waysToWin = 0
for i in range(int(time)):
    if i * (int(time)-i) > int(distance):
        waysToWin += 1
print(waysToWin)