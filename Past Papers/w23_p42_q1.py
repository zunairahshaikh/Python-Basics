#Q1ai

#DECLARE StackVowel: ARRAY[0:100] OF STRING
StackVowel = []
#DECLARE StackConsonant: ARRAY[0:100] OF STRING
StackConsonant = []

#Q1aii
#DECLARE VowelTop AS INTEGER
#DECLARE ConsonantTop AS INTEGER
global VowelTop
global ConsonantTop
VowelTop = 0
ConsonantTop = 0

#Q1bi
def PushData(inLetter):
    global VowelTop
    global ConsonantTop
    if inLetter == "a" or inLetter == "o"  or inLetter == "e" or inLetter == "i" or inLetter == "u":
        if VowelTop == 100:
            print("The stack is full")
        else:
            StackVowel.append(inLetter)
            VowelTop+=1
    else:
        if ConsonantTop == 100:
            print("The stack is full")
        else:
            StackConsonant.append(inLetter)
            ConsonantTop+=1

#Q1bii
def ReadData():
    try:
        fileHandle = open("StackData.txt", "r")
        for oneLine in fileHandle:
            oneLine = fileHandle.readline()
            PushData(oneLine.strip())
        fileHandle.close()
    except:
        print("The file does not exist")

ReadData()
print(StackConsonant)
print(StackVowel)
print(ConsonantTop)
print(VowelTop)
#Q1c
def PopVowel():
    global VowelTop
    if VowelTop - 1 <= 0:
        return "no data"
    else:
        VowelTop -= 1
        dataToReturn = StackVowel[VowelTop]
        del StackVowel[-1]
        return dataToReturn

def PopConsonant():
    global ConsonantTop
    if ConsonantTop - 1 <= 0:
        return "no data"
    else:
        ConsonantTop -= 1
        dataToReturn = StackConsonant[ConsonantTop]
        del ConsonantTop[-1]
        return dataToReturn

#Q1di
ReadData()
for i in range(5):
    letters = ""
    userIn = input("Choose an option: vowel or consonant: ")
    if userIn == "vowel":
        letters = letters + PopVowel()
    else:
        letters += PopConsonant()
print(letters)