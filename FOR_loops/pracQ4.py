#Q4 ask user for the size of a pyramid and output a pyramid of that basesize

basesize = int(input("Enter size of pyramid:"))


for i in range(1, basesize + 1):
    # Print spaces
    print(" " * (basesize - i), end="")

    # Print asterisks for the left half of the pyramid
    for j in range(1, i + 1):
        print("*", end=" ")

    # Print a newline to move to the next row
    print()