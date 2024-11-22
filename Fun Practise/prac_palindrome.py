#Q) ask user to input a string and check if it's a palindrome or not

##METHOD 1

rev_string = ""

Instring = input("Enter your word(s): ")

for i in range(len(Instring)-1,-1,-1):
    rev_string += Instring[i]

if rev_string.lower() == Instring.lower():
    print("Is a palindrome")


else:
    print("not a palindrome")

##METHOD 2

isPal = True
startpos = 0
endpos = int(len(Instring)/2)
strLen = len(Instring)

while startpos <= endpos and isPal:
    char1 = Instring[startpos]
    char2 = Instring[strLen-startpos-1]

    if char1.lower() != char2.lower():
        isPal = False

    startpos +=1

if isPal == True:
    print("is a palindrome")
else:
    print("not a palindrome")
