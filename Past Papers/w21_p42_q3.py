ArrayNodes = [[0 for i in range(3)]for j in range(20)] #INTEGER
RootPtr = -1 #INTEGER
FreePtr = 0 #INTEGER

def AddNode(ArrayNodes, RootPointer,FreePointer):
    global RootPtr
    global FreePtr
    itemToAdd = int(input("Enter your data: "))
    # print("rp", RootPointer)
    # print("fp", FreePointer)
    if FreePointer <=19:
        ArrayNodes[FreePointer][0] = -1
        ArrayNodes[FreePointer][1] = itemToAdd
        ArrayNodes[FreePointer][2] = -1
        if RootPointer == -1:
            RootPtr = 0
        else:
            placed = False
            CurrentNode = RootPointer
            while placed ==False:
                if itemToAdd < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] ==-1:
                        ArrayNodes[CurrentNode][0] = FreePointer
                        placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] ==-1:
                        ArrayNodes[CurrentNode][2] = FreePointer
                        placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreePtr +=1
    else:
        print("Tree is full")

def PrintAll(ArrayNodes):
    for count in range(len(ArrayNodes)):
        print(ArrayNodes[count][0], ArrayNodes[count][1], ArrayNodes[count][2], end = " ")
        print()

for z in range(10):
    AddNode(ArrayNodes,RootPtr,FreePtr)
PrintAll(ArrayNodes)
