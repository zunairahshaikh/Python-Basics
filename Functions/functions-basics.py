#PROCEDURES = VOID FUNCTIONS
#FUNCTIONS = FRUITFUL FUNCTIONS

#syntax for PROC:
def  inputOddNumber():
    num = 0
    while num % 2== 0:
        num = int(input("enter an odd number: "))
    print("valid number entered")
    #main priogram ends here

inputOddNumber() #calling proc
