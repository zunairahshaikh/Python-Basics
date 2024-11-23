#a
#DECLARE ArrayData : ARRAY[0:9,0:9] OF INTEGER
import random
ArrayData = [[random.randint(1,100) for i in range(10)]for i in range(10)]

#b ii
def PrintArray():
    for i in range(10):
        for j in range(10):
            print(ArrayData[i][j], " ", end = "")
        print(" ")

print("before")
PrintArray()
print(" ")

#b i
for x in range(10):
    for y in range(10-1):
        for z in range(10-y-1):
            if ArrayData[x][z] > ArrayData[x][z+1]:
                TempValue = ArrayData[x][z]
                ArrayData[x][z] =ArrayData[x][z+1]
                ArrayData[x][z + 1] = TempValue

print("after")
PrintArray()
print(" ")

#c
def BinarySearch(SearchArray, Lower,Upper,SearchValue):
    if Upper >= Lower:
        Mid = int((Lower+ (Upper-1))/2)
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        elif SearchArray[0][Mid] > SearchValue:
            return BinarySearch(SearchArray, Lower,Mid-1,SearchValue)
        else:
            return BinarySearch(SearchArray, Mid+1,Upper,SearchValue)
    return -1

BinarySearch(ArrayData,1,100,87)
BinarySearch(ArrayData,1,100,71)