from array import *
arr = []
with open("C:\\Users\\Josh\\Documents\\advent of code\\day 3\\input.txt", 'r') as f:
        for line in f.readlines():
            arr.append(line)

#Use data to find points
valid_symbols = "!@#$%^&*()_-+={}/\\[]"
countX = 0
total = 0
for x in arr:
  countY = 0
  flag = 0
  for y in x:
    if flag == 0:
      if arr[countX][countY].isdigit():
        currentNum = "0"
        if countY == 140 or arr[countX][countY+1].isdigit() == False:
          currentNum = arr[countX][countY]            
        elif countY == 139 or arr[countX][countY+2].isdigit() == False:
          currentNum = arr[countX][countY]+arr[countX][countY+1]
          flag = 1
        elif countY == 138 or arr[countX][countY+3].isdigit() == False:
          currentNum = arr[countX][countY]+arr[countX][countY+1]+arr[countX][countY+2]
          flag = 2

        #first column
        countX = int(countX)
        countY = int(countY)
        if countX == 1:
          print (currentNum)
        if countY == 0:
          for i in range(0, countY+currentNum.__len__()+1):
            if countX != 0:
              if arr[countX-1][i] in valid_symbols:
                total += int(currentNum)
                break
            if arr[countX][i] in valid_symbols:
              total += int(currentNum)
              break
            if countX != 140:
              if arr[countX+1][i] in valid_symbols:
                total += int(currentNum)
                break
        #last column
        elif countY == 140:
          for i in range(countY-1, countY+currentNum.__len__()):
            if countX != 0:
              if arr[countX-1][i] in valid_symbols:
                total += int(currentNum)
                break
            if arr[countX][i] in valid_symbols:
              total += int(currentNum)
              break
            if countX != 140:
              if arr[countX+1][i] in valid_symbols:
                total += int(currentNum)
                break
        #any other column
        else:
          for i in range(int(countY)-1, countY+currentNum.__len__()+1):
            #top row
            if countX != 0:
              if arr[countX-1][i] in valid_symbols:
                total += int(currentNum)
                break
            #middle row
            if arr[countX][i] in valid_symbols:
              total += int(currentNum)
              break
            #bottom row
            if countX != 139:
              if arr[countX+1][i] in valid_symbols:
                total += int(currentNum)
                break
    else:
      flag -= 1

    countY += 1
  countX += 1

print(total)