class Picture:
    #DECLARE self.__Description : STRING
    #DECLARE self.__Width : INTEGER
    #DECLARE self.__Height: INTEGER
    #DECLARE self.__FrameColour: STRING
    def __init__(self,d,w,h,fc):
        self.__Description = d
        self.__Width = w
        self.__Height = h
        self.__FrameColour = fc

    def GetDescription(self):
        return self.__Description

    def GetHeight(self):
        return self.__Height

    def GetWidth(self):
        return self.__Width

    def GetColour(self):
        return self.__FrameColour

    def SetDescription(self,desc):
        self.__Description = desc


PicArray = [Picture("",0,0,"") for i in range(100)] #DECLARE PicArray(): ARRAY(1:100) OF Picture

def ReadData(PictureArray):
    counter = 0
    try:
        fileHandle = open("Pictures.txt", 'r')
        description = fileHandle.readline().strip()
        while description!= "":
            width = int(fileHandle.readline().strip())
            height = int(fileHandle.readline().strip())
            frame = fileHandle.readline().strip()
            PictureArray[counter] = Picture(description,width,height,frame)
            counter+=1
            description = fileHandle.readline().strip()

        fileHandle.close()
    except IOError:
        print("File does not exist")
    return counter, PictureArray

numOfPics, PicArray = ReadData(PicArray)
frameColour = input('Enter frame colour: ').lower()
maxWidth = int(input("Enter max width of picture: "))
maxHeight = int(input("Enter max height of picture: "))

print("Matches found:")
for i in range(numOfPics):
    if frameColour == PicArray[i].GetColour() and maxWidth <= PicArray[i].GetWidth() and maxHeight <= PicArray[i].GetHeight():
        print(PicArray[i].GetDescription(), PicArray[i].GetHeight(), PicArray[i].GetWidth())