#Q1ai
DataArray = [] #ARRAY[0:24] OF INTEGER

#Q1aii
try:
    fileHandle = open("C:/Users/Aziz/Data.txt", "r") #create path for file using the directory or extract txt file and save to desktop then click and drag to pycharm
    for i in range(25):
        oneLine = fileHandle.readline()
        DataArray.append(int(oneLine))
    fileHandle.close()
except IOError:
    print("File does not exist")


#Q1bi
def PrintArray(DataArray):
    for i in range(len(DataArray)):
        print(DataArray[i], end = " ")

#Q1bii
PrintArray(DataArray)

print()

#Q1c
def linearSearch(DataArray, SearchItem):
    count = 0
    for i in range(len(DataArray)):
        if DataArray[i] == SearchItem:
            count+=1
    return count

#Q1d
SearchItem = int(input("Enter a number between 0-100 to search: "))
while SearchItem <= 0 and SearchItem >= 100:
    SearchItem = int(input("Enter a number between 0-100 to search: "))
count = linearSearch(DataArray,SearchItem)
print("The number {0} is found {1} time(s)".format(SearchItem, count))