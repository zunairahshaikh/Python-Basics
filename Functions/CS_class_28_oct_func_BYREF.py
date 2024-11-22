#python doesnt have BY REF so we update variables

def adjustVaraibleForNextRow(spaces, symbols):
    spaces-=1
    symbols+=2
    return spaces, symbols

#main program starts here

numberOfSpaces = int(input("enter number of spaces: "))
numberOfSymbols = int(input("enter number of symbols: "))
numberOfSpaces,numberOfSymbols = adjustVaraibleForNextRow(numberOfSpaces, numberOfSpaces)

print(numberOfSpaces)
print(numberOfSymbols)