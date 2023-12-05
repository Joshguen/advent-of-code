from array import *

arr = []
with open("C:\\Users\\Josh\\Documents\\advent of code\\day 3\\input.txt", 'r') as f:
        for line in f.readlines():
            arr.append(line)

#Use data to find points
countX = 0
total = 0
for x in arr:
  countY = 0
  for y in x:
    gearValue = 0
    if arr[countX][countY] == "*":
      currentNum = "0"
      for i in range (-1, 2):
        flag = 0
        if arr[countX+i][countY-1].isdigit():
          if int(currentNum) > 0:
            gearValue = int(currentNum)
          if arr[countX+i][countY-2].isdigit() == False:
            #check right
            if arr[countX+i][countY].isdigit() == False:
              currentNum = arr[countX+i][countY-1]
            else:
              if arr[countX+i][countY+1].isdigit() == False:
                currentNum = arr[countX+i][countY-1]+arr[countX+i][countY]
                flag = 1
              else:
                currentNum = arr[countX+i][countY-1]+arr[countX+i][countY]+arr[countX+i][countY+1]
                flag = 2
          else:
            if arr[countX+i][countY-3].isdigit() == False:
              if arr[countX+i][countY].isdigit() == False:
                currentNum = arr[countX+i][countY-2]+arr[countX+i][countY-1]
              else:
                currentNum = arr[countX+i][countY-2]+arr[countX+i][countY-1]+arr[countX+i][countY]
                flag = 1
            else:
              currentNum = arr[countX+i][countY-3]+arr[countX+i][countY-2]+arr[countX+i][countY-1]
          if gearValue > 0:
            gearValue *= int(currentNum)
        #middle
        if flag < 1:
          if arr[countX+i][countY].isdigit():
            if int(currentNum) > 0:
              gearValue = int(currentNum)
            if arr[countX+i][countY+1].isdigit() == False:
              currentNum = arr[countX+i][countY]
            elif arr[countX+i][countY+2].isdigit() == False:
              currentNum = arr[countX+i][countY]+arr[countX+i][countY+1]
              flag = 2
            else:
              currentNum = arr[countX+i][countY]+arr[countX+i][countY+1]+arr[countX+i][countY+2]
              flag = 2
            if gearValue > 0:
              gearValue *= int(currentNum)
            if countX == 103:
                  print(currentNum)
        #right:
        if flag < 2:
          if arr[countX+i][countY+1].isdigit():
            if int(currentNum) > 0:
              gearValue = int(currentNum)
            if arr[countX+i][countY+2].isdigit() == False:
              currentNum = arr[countX+i][countY+1]
            elif arr[countX+i][countY+3].isdigit() == False:
              currentNum = arr[countX+i][countY+1]+arr[countX+i][countY+2]
            else:
              currentNum = arr[countX+i][countY+1]+arr[countX+i][countY+2]+arr[countX+i][countY+3]
            if gearValue > 0:
              gearValue *= int(currentNum)
      if gearValue > 0:
        total += gearValue
    countY += 1
  countX += 1

print(total)