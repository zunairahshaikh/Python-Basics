#a
class Card:
    #DECLARE self.__Number :INTEGER
    #DECLARE self.__Colour :STRING
    def __init__(self,n,c):
        self.__Number = n
        self.__Colour = c

    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour

#DECLARE cardData: ARRAY(0:29) OF Card
cardData = [0 for x in range(30)]
try:
    fileHandle = open("CardValues.txt", "r")
    for i in range(30):
        num = int(fileHandle.readline())
        colour = fileHandle.readline()
        cardData[i] = Card(num,colour)
except:
    print("File not found")

def ChooseCard():
    takenCards =[]
    isTaken = False
    choiceIndex = int(input("Choose a card between 1 and 30: "))
    while choiceIndex < 1 and choiceIndex > 30:
        choiceIndex = int(input("Choose a card between 1 and 30: "))
    if isTaken:
        takenCards.append(choiceIndex-1)
        print("Card alr taken, pick another")
        return ChooseCard
    else:
        isTaken = True
        return (choiceIndex-1)

ChooseCard()