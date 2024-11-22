#Q make a function that calls another function that takes input and validates if its positive. output multiplication table of the number in the first function

def posNum(userNum):
    while userNum <= 0:
        userNum = int(input("enter a positive number: "))
    return userNum
numb =int(input("enter a number: "))
numb = posNum(numb)
for i in range(1,11):
    multiple = numb * i
    print(f"{numb} * {i} = {multiple}")