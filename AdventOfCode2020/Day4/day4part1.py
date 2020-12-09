with open("input.txt", "r") as f:
    lines = f.readlines()
    numberOfValidPasswords = 0
    passports = []
    currentPassportLine = ""
    for line in lines:
        currentLine = line.strip()
        if currentLine != "":
            currentPassportLine = currentPassportLine + currentLine
        else:
            passports.append(currentPassportLine)
            currentPassportLine = ""
    for passport in passports:
        if passport.count("iyr") > 0 and passport.count("byr") > 0 and passport.count("eyr") and passport.count("hgt") and passport.count("hcl") and passport.count("ecl") and passport.count("pid"):
            numberOfValidPasswords = numberOfValidPasswords + 1
print("The number of valid passwords is: " + str(numberOfValidPasswords))