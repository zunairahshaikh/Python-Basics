#Q ask user for their name and output all even position characters fist then output all odd position charaters

name = input("Your good name sir?: ")
namelen = len(name)
evenstring = ""
oddstring = ""
for i in range (1,namelen+1):
    if i % 2 ==0:
        evenstring += name[i-1]
    else:
        oddstring += name[i-1]

print(evenstring)
print(oddstring)
