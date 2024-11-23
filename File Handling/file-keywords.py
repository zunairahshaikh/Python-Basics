#open(filename, mode)
#w = WRITE(creates files/ recreates files, store data, add \n to change line)
#R = READ(req: file should exist, fetches data)
#A = APPEND (req: file should exist,  adds data to end of the file), there is no <file.append> function, write <file.write> w/ mode "a"

fileHandle = open("sampleFile.TXT", 'w')
fileHandle.write("line of text to store \n")
fileHandle.write('this is my second line \n')
fileHandle.close()

fileHandle = open("sampleFile.TXT", 'r')
lineOfText = fileHandle.readline()
print(lineOfText)
fileHandle.close()

fileHandle = open("sampleFile.TXT", 'a')
lineOfText = "appended line"
fileHandle.write(lineOfText)
fileHandle.close()

#Q1) create a file called names.txt and ask user to store names in the file
namesHandle = open("names.txt", 'w')
for i in range(5):
    name = input("enter a name:")
    namesHandle.write(name + "\n")
namesHandle.close()

#Q2) read file "names.txt" and copy all names less than 5 characters in a new file "favnames.txt"

newFile = open("FavNames.txt", 'w')
namesHandle = open('names.txt', 'r')

for j in range(5):
    nameInLine = namesHandle.readline().strip()
    if len(nameInLine) < 5:
        newFile.write(nameInLine +'\n')
namesHandle.close()
newFile.close()

print("Umama <3")
