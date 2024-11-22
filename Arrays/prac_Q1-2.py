#Q) create an array and ask user to enter 10 names into the array

i = 0
names = []
for i in range(0,10):
    usernames = input("naam pls: ")
    names.append(usernames)

print(names)
print()


#Q) ask the user for a name in the array and output its index or output not found

userfind = input("Which name do you want to find?: ")
for j in range(len(names)):
    if names[j] == userfind:
        index_of_name = j
        print("this name is stored at index ",j)
        break
if  names[j] != userfind:
    print("not found")



