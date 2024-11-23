#a
headPointer = 0 #DECALRE headpointer : INT
tailPointer =0  #DECALRE tailPointer :INT
QueueArray = ["" for i in range(10)] # DECLARE QueueArray() : ARRAY(0:9) OF STRING
NumberItems = 0
#b
def Enqueue(DataToAdd):
    global tailPointer
    global NumberItems
    if NumberItems == 10:
        return  False
    QueueArray[tailPointer] = DataToAdd
    if tailPointer >=9:
        tailPointer=0
    else:
        tailPointer+= 1
    NumberItems+=1
    return True

#c
def Dequeue():
    global headPointer
    if len(QueueArray) ==0:
        return False
    itemToReturn = QueueArray[headPointer]
    headPointer += 1
    return itemToReturn

#d i
for x in range(11):
    userInput = input("Enter a string: ")
    if Enqueue(userInput):
        print("addition successful")
    else:
        print("addition unsuccessful")
print(Dequeue())
print(Dequeue())