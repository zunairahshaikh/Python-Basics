#Function w/out parameter
def  inputOddNumber():
    num = 0
    while num % 2== 0:
        num = int(input("enter an odd number: "))
    return num
    #main priogram ends here

newnum = inputOddNumber()
print("return value is", newnum)

print()

#Function w/ parameter

def sumRange(firstnum, lastnum):
    sum = 0
    for thisnum in range(firstnum, lastnum+1):
        sum += thisnum
    return sum

newnum = sumRange(1,18)
print(newnum)
