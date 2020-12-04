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
    firstPos = int(numbers[0]) - 1 #Should be 1
    secondPos = int(numbers[1]) - 1 #Should be 2
    letterToLookFor = sections[1][0]
    print("letterToLookFor = " + letterToLookFor)
    password = sections[2].strip()
    print("password = " + password)
    numberOfTimesLetterInPassword = 0
    if password[firstPos] == letterToLookFor:
        numberOfTimesLetterInPassword = numberOfTimesLetterInPassword + 1
    if password[secondPos] == letterToLookFor:
        numberOfTimesLetterInPassword = numberOfTimesLetterInPassword + 1
    print("number of times letter found = " + str(numberOfTimesLetterInPassword))
    if numberOfTimesLetterInPassword == 1:
        print("valid one found")
        numberOfValidPasswords = numberOfValidPasswords + 1
print("Number of valid passwords = " + str(numberOfValidPasswords))
