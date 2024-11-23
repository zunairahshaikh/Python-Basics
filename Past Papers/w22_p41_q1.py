#a)
DataArray = [] #ARRAY [0:99} OF INTEGER

#b)
def ReadFile():
    try:
        fileHandle = open("IntegerData.txt", "r")
        for oneLine in fileHandle:
            DataArray.append(int(oneLine.strip()))
        fileHandle.close()
    except IOError:
        print("file does not exist")

#c)
def FindValues():
    userInput = int(input("Enter a number between 1-100: "))
    while userInput < 1 or userInput > 100:
        userInput = int(input("Enter a number between 1-100: "))
    count = 0
    for num in DataArray: #num = DataArray[index]
        if num == userInput:
            count += 1
    return count

#e)
def BubbleSort():
    for i in range(len(DataArray)-1):
        for j in range(len(DataArray)-1-i):
            if DataArray[j] > DataArray[j+1]:
                temp = DataArray[j]
                DataArray[j] = DataArray[j+1]
                DataArray[j + 1] = temp


#d)
ReadFile()
retCount = FindValues()
print("The number repeats",retCount,"times")
BubbleSort()
print(DataArray)
