f = open("Part1Input.txt", "r")
lines = ["0"]
for strLine in f:
    lines.append(strLine)

for i in range(0, len(lines)):
    #print (lines[i])
    #input("waiting for input.")
    for j in range (i, len(lines)):
        for k in range(j, len(lines)):
            total = int(lines[i]) + int(lines[j]) + int(lines[k])
        #print(total)
            if total == 2020:
                multiplyTotal = int(lines[i]) * int(lines[j]) * int(lines[k])
                print('Winning number is ' + str(multiplyTotal))
