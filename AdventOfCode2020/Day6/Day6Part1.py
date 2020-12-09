def removeDuplicate(str): 
    t="" 
    for i in str: 
        if(i in t): 
            pass
        else: 
            t=t+i
    return t
    
with open("input.txt", "r") as f:
    lines = f.readlines()
    numberOfYes = 0
    replies = []
    currentReplyLine = ""
    for line in lines:
        currentLine = line.strip()
        #print (currentLine)
        if currentLine != "":
            currentReplyLine = currentReplyLine + currentLine
        else:
            replies.append(currentReplyLine)
            currentReplyLine = ""
    replies.append(currentReplyLine)
    for reply in replies:
        #print (reply)
        reply = removeDuplicate(reply)
        print(reply)
        numberOfYes = numberOfYes + len(reply)
print("The number of yes replies is: " + str(numberOfYes))