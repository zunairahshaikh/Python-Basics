#Q3 ask user for their name and output a decorated sign
#eg name = zun
# ******
# *ZUN**
# ******


#len of nam
#for stars, print # more stars than the name len
#one star each side, space after star
middleString = ""
name = input("yooooo aap ka naam? ")

nameLen = len(name)

print("*"*(nameLen+3))
middleString = "*" + name + '**'
print (middleString)
print("*"* (nameLen+3))