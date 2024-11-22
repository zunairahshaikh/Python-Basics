#Q) ask user to input a string and output its reverse

rev_string = ""

Instring = input("Enter your word(s): ")

for i in range(len(Instring)-1,-1,-1):
    rev_string += Instring[i]

print(rev_string)