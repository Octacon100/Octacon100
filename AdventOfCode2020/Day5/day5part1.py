import math

maxSeatId = 0
maxRowRange = 127
maxColumnRange = 7


#Seems like dividing everything in half, then taking ceiling or floor depending on F (lower half) or B(upper half)
#with open("testinput.txt", "r") as f:
with open("input.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        seatRow = 0
        seatColumn = 0
        currentMaxRowRange = maxRowRange
        currentMinRowRange = 0
        currentMaxColumnRange = maxColumnRange
        currentMinColumnRange = 0
        #print ("Max = " + str(currentMaxRowRange) + " Min = " + str(currentMinRowRange))
        for i in range(0, 6):
            char = line[i].strip()
            #print(char)
            if char == "F":
                #lower half
                currentMaxRowRange = math.floor((currentMaxRowRange + currentMinRowRange) / 2)
                seatRow = currentMaxRowRange
            elif char == "B":
                #higher half
                currentMinRowRange = math.ceil((currentMaxRowRange + currentMinRowRange) / 2)
                seatRow = currentMinRowRange
            else:
                print("Dunno what happened here on the row man with " + char)
            #print ("Max row = " + str(currentMaxRowRange) + " Min row = " + str(currentMinRowRange))
        
        #print ("Seat Row = " + str(seatRow))
        for i in range(7, 10):
            char = line[i].strip()
            if char == "L":
                #lower half
                currentMaxColumnRange = math.floor((currentMaxColumnRange + currentMinColumnRange) / 2)
                seatColumn = currentMinColumnRange
            elif char == "R":
                #higher half
                currentMinColumnRange = math.ceil((currentMaxColumnRange + currentMinColumnRange) / 2)
                seatColumn = currentMaxColumnRange
            else:
                print("Dunno what happened here on the row man with " + char)
            #print ("Max column = " + str(currentMaxColumnRange) + " Min column = " + str(currentMinColumnRange))
        #print ("Seat column = " + str(seatColumn))

        seatId = (seatRow * 8) + seatColumn
        #print ("Seat details = " + line + " gives an index of " + str(seatId))
        if seatId > maxSeatId:
            maxSeatId = seatId
            print ("New Max: Seat details = " + line + " gives an index of " + str(seatId))

print("Max Seat ID = " + str(maxSeatId))        