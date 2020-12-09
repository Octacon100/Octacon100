import ast
import re
with open("input.txt", "r") as f:
    lines = f.readlines()
    numberOfValidPasswords = 0
    passports = []
    currentPassportLine = ""
    for line in lines:
        currentLine = line.replace('\n', ' ')
        if line.strip() != "":
            currentPassportLine = currentPassportLine + currentLine
        else:

            currentPassportLine = currentPassportLine.strip().replace(" ", ", ").replace(",, ", ", ")
            passports.append(currentPassportLine)
            currentPassportLine = ""
    for passport in passports:
        if passport.count("iyr") > 0 and passport.count("byr") > 0 and passport.count("eyr") and passport.count("hgt") and passport.count("hcl") and passport.count("ecl") and passport.count("pid"):
            print(passport)
            #Make a dictionary
            passport_dict = dict((x.strip(), y.strip())
                         for x, y in (element.split(':')
                         for element in passport.split(', ')))
            #print(passport_dict)
            
            #Now we have the dictionary, check it.
                # byr (Birth Year) - four digits; at least 1920 and at most 2002.
            byrValid = 0
            if int(passport_dict["byr"]) >= 1920 and int(passport_dict["byr"]) <= 2002:
                byrValid = 1
                print("Valid Birthyear.")
                # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
            iyrValid = 0
            if int(passport_dict["iyr"]) >= 2010 and int(passport_dict["iyr"]) <= 2020:
                iyrValid = 1
                print("Valid issue year.")
                # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
            eyrValid = 0
            if int(passport_dict["eyr"]) >= 2020 and int(passport_dict["eyr"]) <= 2030:
                eyrValid = 1
                print("Valid exp year.")
                # hgt (Height) - a number followed by either cm or in:
                #find the first position of c or i.
                # If cm, the number must be at least 150 and at most 193.
                # If in, the number must be at least 59 and at most 76.
            hgtValid = 0
            numberEnd = 0
            if "cm" in passport_dict["hgt"] or "in" in passport_dict["hgt"]:
                if "cm" in passport_dict["hgt"]:
                    numberEnd = passport_dict["hgt"].index("c")
                    height = int(passport_dict["hgt"][0:numberEnd])
                    if height >= 150 and height <= 193:
                        hgtValid = 1
                        print("Valid height by centimeters.")
                if "in" in passport_dict["hgt"]:
                    numberEnd = passport_dict["hgt"].index("i")
                    height = int(passport_dict["hgt"][0:numberEnd])
                    if height >= 59 and height <= 76:
                        hgtValid = 1
                        print("Valid height by inches.")
                
                # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
            hclValid = 0
            print(passport_dict["hcl"])
            if passport_dict["hcl"][0] == "#" and len(passport_dict["hcl"]) == 7:
                if re.match("^[a-z0-9]*$", passport_dict["hcl"][1:6] ):
                    hclValid = 1
                    print("Valid Haircolor.")
                # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
            eclValid = 0
            validEyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if passport_dict["ecl"] in validEyeColors:
                eclValid = 1
                print("Valid eye color.")
                # pid (Passport ID) - a nine-digit number, including leading zeroes.
            pidValid = 0
            if len(passport_dict["pid"]) == 9 and passport_dict["pid"].isdecimal():
                pidValid = 1
                print("Valid passport.")
                # cid (Country ID) - ignored, missing or not.
            if (byrValid + iyrValid + eyrValid + hgtValid + hclValid + eclValid + pidValid) == 7:
                numberOfValidPasswords = numberOfValidPasswords + 1

print("The number of valid passwords is: " + str(numberOfValidPasswords))
    # currentPosX = 0
    # currentPosY = 0
    # slopeX = 3
    # slopeY = 1
    # numberOfTrees = 0
    # # print(len(lines[0]))
    # # print(lines[0])
    # while currentPosY < len(lines):
    #     # if lines[currentPosY][currentPosX] == ".":
    #     #     numberOfTrees = numberOfTrees #Do nothing.
    #     if lines[currentPosY][currentPosX] == "#":
    #         numberOfTrees = numberOfTrees + 1 #You hit a tree.
    #     currentPosX = currentPosX + slopeX
    #     currentPosY = currentPosY + slopeY
    #     if currentPosX >= len(lines[0]) - 1:
    #         print("End of line at: " + str(currentPosX))
    #         print("Length of line: " + str(len(lines[0])))
    #         currentPosX = currentPosX - len(lines[0]) + 1
    #         print("Current Pos after move: " + str(currentPosX))
    # print("Number of trees hit:" + str(numberOfTrees))
