f = file("input.txt", "r")
lines = f.readlines()

numberOfValidPasswords = 0

for line in lines:
    print(line)
    sections = line.split(" ")
    #Process 1-2 x: xpxc
    #1st step, process 1-2
    #print(sections[0])
    #print(sections)
    numbers = sections[0].split("-")
    #print(numbers)
    minNumber = numbers[0] #Should be 1
    maxNumber = numbers[1] #Should be 2
    letterToLookFor = sections[1][0]
    print("letterToLookFor = " + letterToLookFor)
    password = sections[2].strip()
    print("password = " + password)
    numberOfTimesLetterInPassword = password.count(letterToLookFor)
    print("number of times letter found = " + str(numberOfTimesLetterInPassword))
    if numberOfTimesLetterInPassword >= int(minNumber) and numberOfTimesLetterInPassword <= int(maxNumber):
        print("valid one found")
        numberOfValidPasswords = numberOfValidPasswords + 1
print("Number of valid passwords = " + str(numberOfValidPasswords))
