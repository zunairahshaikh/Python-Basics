#a
arrayData = [10,5,6,7,1,12,13,15,21,8]

#bi
def linerSearch(searchItem):
    for item in arrayData: #item will directly copy from the list
        if item == searchItem:
            return True
    return False

#bii
userInput = int(input("Enter a value to search: "))
retVal = linerSearch(userInput)
if retVal == True:
    print("Value found in list")
else:
    print("Value not found")

#c
def bubbleSort():
    for x in range(len(arrayData)):
        for y in range(len(arrayData)-1): #so that second last value is compared with last val
            if arrayData[y] < arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y + 1] = temp

bubbleSort()
print(arrayData)