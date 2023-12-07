import re
f = open("C:\\Users\\Josh\\Documents\\advent of code\\day 5\\input.txt", "r")
xCount = 0
seeds, seedSoil, soilFert, fertWater, waterLight, lightTemp, tempHum, humLoc = ([] for i in range(8))
lowestLoc = 100000000000
maps = [seedSoil, soilFert, fertWater, waterLight, lightTemp, tempHum, humLoc]
for x in f:
    match xCount:
        case 0:
            seeds = re.findall(r'\d+',x)
        case xCount if 3 <= xCount < 15:
            seedSoil.append(re.findall(r'\d+',x))
        case xCount if 17 <= xCount < 34:
            soilFert.append(re.findall(r'\d+',x))
        case xCount if 36 <= xCount < 75:
            fertWater.append(re.findall(r'\d+',x))
        case xCount if 77 <= xCount < 118:
            waterLight.append(re.findall(r'\d+',x))
        case xCount if 120 <= xCount < 152:
            lightTemp.append(re.findall(r'\d+',x))
        case xCount if 154 <= xCount < 196:
            tempHum.append(re.findall(r'\d+',x))
        case xCount if 198 <= xCount < 244:
            humLoc.append(re.findall(r'\d+',x))
    xCount += 1
for i in range(0, len(seeds), 2):
    print(i)
    for j in range(int(seeds[i]), int(seeds[i])+int(seeds[i+1])):
        finalLocation = j
        for map in maps:
            for equivalent in map:
                if finalLocation >= int(equivalent[1]) and finalLocation < (int(equivalent[1])+int(equivalent[2])):
                    finalLocation = int(equivalent[0]) + finalLocation - int(equivalent[1])
                    break
        if int(finalLocation) < lowestLoc:
            lowestLoc = int(finalLocation)
print (lowestLoc)
