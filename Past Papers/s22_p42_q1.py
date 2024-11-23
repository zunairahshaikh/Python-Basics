#a
StackData =[]
StackData = [0,0,0,0,0,0,0,0,0,0]
StackPointer =0 #INT

#b
def OutputStackData():
    global StackPointer
    for i in range(len(StackData)):
        print(StackData[i])
    print(StackPointer)

#c
def Push(userInput):
    global StackPointer
    if StackPointer == len(StackData):
        return False
    else:
        StackData[StackPointer] = userInput
        StackPointer+= 1
        return True

#d
for x in range(11):
    addVal = int(input("Enter a number: "))
    if Push(addVal):
        print("addition successful")
    else:
        print("addition unsuccessful. stack is full")
print(StackData)

#e i
def Pop():
    global StackPointer
    if StackPointer == 0:
        return -1
    else:
        retVal = StackData[StackPointer-1]
        StackPointer -= 1
        return retVal

#e ii
Pop()
Pop()
print(StackData)