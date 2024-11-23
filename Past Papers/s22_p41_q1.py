#a
#DECLARE playerInfo : ARRAY [[0:10] 0:10] OF STRING
playerInfo = [["" for x in range(2)] for j in range(10)]
newInfoList = [["" for i in range(2)] for j in range(10)]


#b
def ReadHighScore():
    try:
        fileHandle = open ("HighScore.txt", "r")
        for i in range(10):
            playerInfo[i][0] = fileHandle.readline() [:3] #left p name hai
            playerInfo[i][1] = int(fileHandle.readline())

    except:
        print("file not found")


#c
def OutputHighScores():
    for i in range(10):
        print(playerInfo[i][0], playerInfo[i][1])

#d i
ReadHighScore()
OutputHighScores()


#e i
newPlayerName = input("Enter a 3 character name: ")
while len(newPlayerName) != 3:
    newPlayerName = input("Enter a 3 character name: ")
newPlayerScore = int(input("Enter score: "))
while newPlayerScore < 1 and newPlayerScore > 1000000:
    newPlayerScore = int(input("Enter score: "))

#e ii
def NewScoreList(PlayerName, PlayerScore):
    lowest = playerInfo[9][1]
    found = 0

    #if newPlayerScore < lowest:
    #     return

    for x in range(10):
        if (newPlayerScore > int(playerInfo[x][1])) and (found == 0) :
            newInfoList[x][0] = PlayerName
            newInfoList[x][1] = PlayerScore
            found = 1
        else:
            newInfoList[x+found][0] = playerInfo[x][0]
            newInfoList[x+found][1] = playerInfo[x][1]

NewScoreList(newPlayerName,newPlayerScore)

print(newInfoList)

#???????????????