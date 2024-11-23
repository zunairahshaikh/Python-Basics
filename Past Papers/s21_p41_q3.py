#a
class TreasureChest():
    # DECLARE self.__question: STRING
    # DECLARE self.__answer: INTEGER
    # DECLARE self.__points: INTEGER
    def __init__(self,q,a,p):
        self.__question = q
        self.__answer = a
        self.__points =p

    #c i
    def getQuestion(self):
        return self.__question

    #c ii
    def checkAnswer(self,userAns):
        if userAns == self.__answer:
            return True
        else:
            return False

    #c iii
    def getPoints(self, attempts):
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return int(self.__points//2) #int division is //
        elif attempts == 3 or attempts==4:
            return int(self.__points//4)
        else:
            return 0

#b
arrayTreausure =[]
def readData():
    try:
        fileHandle = open("TreasureChestData.txt", "r")
        ques =  fileHandle.readline().strip()
        while len(ques) >0:
            ans = int(fileHandle.readline().strip())
            pts = int(fileHandle.readline().strip())
            arrayTreausure.append(TreasureChest(ques, ans,pts))
            ques = fileHandle.readline().strip()
        fileHandle.close()
    except:
        print("File not found")

#c iv
readData()
userChoice = int(input("Enter a question number between 1-5: "))
if userChoice >0 and userChoice <6:
    result = False
    userAttempts = 0
    while result == False:
        userAns = int(input(arrayTreausure[userChoice-1].getQuestion() ))
        result = arrayTreausure[userChoice-1].checkAnswer(userAns)
        userAttempts +=1
    print("You have won", int(arrayTreausure[userChoice-1].getPoints(userAttempts)), "points")