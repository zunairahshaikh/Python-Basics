list1 =[]
list1.append("watermelons")
list1.append ("apples")
list1.append("peaches")

print("vale at index 2 is =", list1[2])
print('length of list 1 is =', len(list1))
list1[2] = "anar"
print("vale at index 2 is =", list1[2])
for i in range(len(list1)):
    print(list1[i])

#arrayname = {initial value for i in range(size)}
list3 = [0 for i in range(100)]
print("list 3 values")
for i in  range(len(list3)):
    print("index", i, "=", list3[i])