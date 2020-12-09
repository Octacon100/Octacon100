class Reply:
    def __init__(self, replyLine, numberOfPeople):
        self.replyLine = replyLine
        self.numberOfPeople = numberOfPeople

    def getReplyAllYesCount(self):
        allYesCount = 0
        for letterToLookFor in self.removeDuplicate():
            print (letterToLookFor)
            if self.numberOfPeople == self.replyLine.count(letterToLookFor):
                allYesCount = allYesCount + 1
        print (str(allYesCount) + " is the all yes count.")
        return allYesCount

    def removeDuplicate(self): 
        t="" 
        for i in self.replyLine: 
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
    numberOfPeople = 0
    for line in lines:
        currentLine = line.strip()
        #print (currentLine)
        if currentLine != "":
            currentReplyLine = currentReplyLine + currentLine
            numberOfPeople = numberOfPeople + 1
        else:
            reply = Reply(currentReplyLine, numberOfPeople)
            replies.append(reply)
            currentReplyLine = ""
            numberOfPeople = 0
    #Add the last group
    reply = Reply(currentReplyLine, numberOfPeople)
    replies.append(reply)
    for reply in replies:
        #print (reply)
        numberOfYes = numberOfYes + reply.getReplyAllYesCount()
print("The number of yes replies is: " + str(numberOfYes))