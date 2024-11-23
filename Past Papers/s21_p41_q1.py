#a
#record is created as a class in python
#all attributes in records are public
#private: __
#public: nothing required
#if attribute initialization not given, use parameters

class node:
    #self.data : INT
    #self.nextNode : INT
    def __init__(self, thisData, thisNextNode):
        self.data = thisData
        self.nextNode = thisNextNode

#b
linkedList = [node(1,1), node(5,4), node(6,7),node(7,-1),node(2,2), node(0,6), node(0,8), node(56,3), node(0,9), node(0,-1)]
#linkedLit.append(node(dataValue, nextNodeValue)
startPointer = 0
emptyList = 5

#c i
#arrays are by default public in python
def outputNodes(linkedList, startPointer):
    currentPointer = startPointer
    while currentPointer != -1: #while not null pointer, we dont know how many times the loop will run
        print(linkedList[currentPointer].data)
        currentPointer = linkedList[currentPointer].nextNode

#c ii
outputNodes(linkedList,startPointer)

#d i
#emptyList = free list pointer (the pointer for the next empty space)
def addNode(linkedList, startPointer, emptyList):
    if emptyList == -1:
        return False
    else:
        userInput = int(input("Enter the data to add: "))
        thisNode = emptyList
        emptyList = linkedList[emptyList].nextNode
        linkedList[thisNode].data = userInput
        linkedList[thisNode].nextNode = -1
        currentPointer = startPointer
        while currentPointer != -1:
            prevPointer = currentPointer
            currentPointer = linkedList[currentPointer].nextNode
        linkedList[prevPointer].nextNode = thisNode
        return True

#d ii
retVal = addNode(linkedList,startPointer,emptyList)
if retVal == True:
    print("Value added")
else:
    print("linked list is full")
outputNodes(linkedList, startPointer)