#a
class Balloon:
    # DECLARE self.__Health: INTEGER
    # DECLARE self.__Colour: STRING
    # DECLARE self.__DefenceItem: STRING
    def __init__(self,c,di):
        self.__Health = 100
        self.__Colour = c
        self.__DefenceItem = di

     #b
    def GetDefenceItem(self):
        return self.__DefenceItem

    #c
    def ChangeHealth(self,healthAdd):
        self.__Health += healthAdd

    #d
    def CheckHealth(self):
        if self.__Health >0:
            return False
        else:
            return True

#e
userDefItem = input("Enter a defence item for the balloon: ")
userColor = input("Enter a color for the balloon: ")
Balloon1 = Balloon(userColor,userDefItem)

#f
def Defend(NewBalloon):
    balloonStrength = int(input("Enter the strength of the opponent: "))
    NewBalloon.ChangeHealth(-balloonStrength)
    print(NewBalloon.GetDefenceItem())
    NewBalloon.CheckHealth()
    if NewBalloon.CheckHealth() == True:
        print("health remaining")
    else:
        print("no health remaining moye moye")
    return NewBalloon

#g
Balloon1=Defend(Balloon1)