# BUILT-IN FUNCTIONS

mystr = input("enter smth: ")

#MID
print(mystr[2:6])
print(mystr[0:5])
#*******************

#LEFT
print(mystr[:7])
print(mystr[:-5])
#*******************

#RIGHT
print(mystr[2:])
print(mystr[-7:])
#******************

#UPPER AND LOWER CASE
print(mystr.upper())
print(mystr.lower())
#********************

#INT() (STRING TO INTEGER)
mynum = 7.99
print(int(mynum)) #chops off decimal numbers not round off

strnum = "7"
#if we write print(strnum +2 it will give an error)
print(int(strnum)+2)
#*********************

#FLOAT (STRING TO FLOAT)
strfloat = "7.55"
#cant use int() for float numbers
print(float(strfloat))
print(float(strfloat)+2.9)