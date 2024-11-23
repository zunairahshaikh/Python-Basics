#a
ArrayNodes = []
for i in range(20):
    ArrayNodes.append([-1,-1,-1])

#b
ArrayNodes = [[1,20,5], [2,15,-1],[-1,3,3],[-1,9,4],[-1,10,-1],[-1,58,-1],[-1,-1,-1]]
FreeNode = 6
RootPointer = 0

#c
def SearchValue(Root, ValueToFind):
    #global ArrayNodes
    if Root == -1:
        return -1
    elif ArrayNodes[Root][1] == ValueToFind:
            return Root
    elif ArrayNodes[Root][1] == -1: #ArrayNodes[root][1] means the data of that node
                return -1
    if ArrayNodes[Root][1] > ValueToFind:
        return SearchValue(ArrayNodes[Root][0],ValueToFind) #traversing left
    if ArrayNodes[Root][1] < ValueToFind:
        return SearchValue(ArrayNodes[Root][2], ValueToFind) #traversing right

#d
def PostOrder(RootNode):
    #global ArrayNodes
    if ArrayNodes[RootNode][0] != -1:
        PostOrder(ArrayNodes[RootNode][0])
    if ArrayNodes[RootNode][2] != -1:
        PostOrder(ArrayNodes[RootNode][2])
    print(str(ArrayNodes[RootNode][1]))

retVal = SearchValue(RootPointer,15)
if retVal == -1:
    print("Value not found")
else:
    print("Value found at ", retVal)
PostOrder(RootPointer)