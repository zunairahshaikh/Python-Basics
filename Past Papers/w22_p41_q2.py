#a)
class Card:
    # self.__Number: INTEGER
    # self.__Colour: STRING

    def __init__(self,n,c):
        self.__Number = n
        self.__Colour = c

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour

red1 = Card(1,"red")
red2 = Card(2,"red")
red3 = Card(3,"red")
red4 = Card(4,"red")
red5 = Card(5,"red")
blue1 = Card(1, "blue")
blue2 = Card(2, "blue")
blue3 = Card(3, "blue")
blue4 = Card(4, "blue")
blue5 = Card(5, "blue")
yellow1 = Card(1, "yellow")
yellow2 = Card(2, "yellow")
yellow3 = Card(3, "yellow")
yellow4 = Card(4, "yellow")
yellow5 = Card(5, "yellow")

class Hand:
    # self.__Cards: ARRAY[0:9] OF Card
    # self.__FirstCard: INTEGER
    # self.__NumberCards: INTEGER

    def __init__(self, c1,c2,c3,c4,c5):
        self.__Cards = [c1, c2, c3, c4, c5]
        self.__FirstCard = 0
        self.__NumberCards = 5

    def GetCard(self, index):
        return self.__Cards[index]

player1 = Hand(red1, red2, red3, red4, yellow1)
player2 = Hand(yellow2, yellow3, yellow4, yellow5, blue1)

def CalculateValue(playerHand):
    score = 0
    for i in range(5):
        thisCard = playerHand.GetCard(i)
        if thisCard.GetColour() == "red":
            score+=5
        elif thisCard.GetColour() == "blue":
            score+=10
        else:
            score += 15
    return score

player1Score = CalculateValue(player1)
player2Score = CalculateValue(player2)
if player2Score > player1Score:
    print("Player 2 wins")
elif player1Score > player2Score:
    print("Player 1 wins")
else:
    print("Draw")