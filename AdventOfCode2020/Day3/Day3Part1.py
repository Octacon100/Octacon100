with open("input.txt", "r") as f:
    lines = f.readlines()
    currentPosX = 0
    currentPosY = 0
    slopeX = 3
    slopeY = 1
    numberOfTrees = 0
    # print(len(lines[0]))
    # print(lines[0])
    while currentPosY < len(lines):
        # if lines[currentPosY][currentPosX] == ".":
        #     numberOfTrees = numberOfTrees #Do nothing.
        if lines[currentPosY][currentPosX] == "#":
            numberOfTrees = numberOfTrees + 1 #You hit a tree.
        currentPosX = currentPosX + slopeX
        currentPosY = currentPosY + slopeY
        if currentPosX >= len(lines[0]) - 1:
            print("End of line at: " + str(currentPosX))
            print("Length of line: " + str(len(lines[0])))
            currentPosX = currentPosX - len(lines[0]) + 1
            print("Current Pos after move: " + str(currentPosX))
    print("Number of trees hit:" + str(numberOfTrees))
