# convert pyramid code to use while loop

# ogcode:
# basesize = int(input("Enter size of pyramid:"))
# for i in range(1, basesize + 1):
#   # Print spaces
#  print(" " * (basesize - i), end="")
#
# Print asterisks for the left half of the pyramid
#   for j in range(1, i + 1):
#      print("*", end=" ")
#
# Print a newline to move to the next row
#   print()

base = int(input("Enter size of pyramid:"))

i = 1

while i < base + 1:
    print(" " * (base - i), end="")
    i+=1

j = 1
while j < i + 1:
    print("*", end=" ")
    j +=1

    # correction!!

base = int(input("Enter size of pyramid:"))

i=1
while i < base+1:
    spacenum = base - i
    spaces = 0
    while spaces < spacenum:
        print(" ", end=" ")
        spaces +=1

    symbolnum = (i*2) - 1
    symbols = 0
    while symbols < symbolnum:
        print("*", end=" ")
        symbols+=1

    print()
    i+=1