with open("input.txt", "r") as f:
    lines = f.readlines()
    slopeX = [1, 3, 5, 7, 1]
    slopeY = [1, 1, 1, 1, 2]
    numberOfTreesMultiple = 1
    # print(len(lines[0]))
    # print(lines[0])
    for i in range(len(slopeX)):
        numberOfTrees = 0
        currentPosX = 0
        currentPosY = 0
        while currentPosY < len(lines):
            # if lines[currentPosY][currentPosX] == ".":
            #     numberOfTrees = numberOfTrees #Do nothing.
            if lines[currentPosY][currentPosX] == "#":
                numberOfTrees = numberOfTrees + 1 #You hit a tree.
            currentPosX = currentPosX + slopeX[i]
            currentPosY = currentPosY + slopeY[i]
            if currentPosX >= len(lines[0]) - 1:
                print("End of line at: " + str(currentPosX))
                print("Length of line: " + str(len(lines[0])))
                currentPosX = currentPosX - len(lines[0]) + 1
                print("Current Pos after move: " + str(currentPosX))
        print("Number of trees hit:" + str(numberOfTrees))
        numberOfTreesMultiple = numberOfTreesMultiple * numberOfTrees
    print("Number of trees hit multiple:" + str(numberOfTreesMultiple))
