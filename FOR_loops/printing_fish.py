#Q5 ask user for the number of fishes and size of the fish and print that many fish

fishsize = int(input("Enter the size of the fish: "))
numoffish = int(input("How many fish do you want?: "))

for fish in range(1,numoffish+1):
    #pyramid at the start
    for i in range(1, fishsize + 1):
        # Print spaces
        print(" " * (fishsize - i), end="")
    
        # Print asterisks for the left half of the pyramid
        for j in range(1, i + 1):
            print("*", end=" ")
    
        print()
    
    #ulta pyramid in b/w
    for i in range(fishsize,0,-1):
        # Print spaces
        print(" " * (fishsize - i), end="")
    
        # Print asterisks for the left half of the pyramid
        for j in range(i ,0,-1):
            print("*", end=" ")
    
        print()
    
    #pyramid at end
    for i in range(1, fishsize + 1):
        # Print spaces
        print(" " * (fishsize - i), end="")
    
        # Print asterisks for the left half of the pyramid
        for j in range(1, i + 1):
            print("*", end=" ")
    
        print()
    print()
