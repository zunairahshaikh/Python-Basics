#Q3) create an array to store CS marks for CSC4 which has 65 students, take input for all marks of students

i = 0
CSC4_marks =[]
for i in range(65):
    std_mark = int(input(f"enter marks of student {i+1}: "))
    CSC4_marks.append(std_mark)

print()

#Q4) from task 3 calc avg, highest, lowest marks

highest = CSC4_marks[0]
for h in range(len(CSC4_marks)):
    if highest < CSC4_marks[h]:
        highest = CSC4_marks[h]
print("the highest marks are", highest)

lowest = CSC4_marks[0]
for l in range(len(CSC4_marks)):
    if lowest > CSC4_marks[l]:
        lowest = CSC4_marks[l]
print("the lowest marks are", lowest)

CSC4_marks_avg = sum(CSC4_marks)/len(CSC4_marks)
print(f'the average marks for this class are {CSC4_marks_avg}')

print()

#Q5) create an array to store names of all students in cSC4, same index as marks

n = 0
CSC4_names =[]
for n in range(65):
    std_name = input(f"enter name of student {n+1}: ")
    CSC4_names.append(std_name)

print()

#Q6) output names of students with highest and lowest marks

#use the max and min function
highestMarksIndex = CSC4_marks.index(max(CSC4_marks))
lowestMarksIndex = CSC4_marks.index(min(CSC4_marks))

highestMarkStudent=CSC4_names[highestMarksIndex]
lowestMarksStudent = CSC4_names[lowestMarksIndex]

# all students with the highest mark
students_with_highest_mark = []
for highest_count in range(len(CSC4_marks)):
    if CSC4_marks[highest_count] == highest:
        students_with_highest_mark.append(CSC4_names[highest_count])

#all students with the lowest mark
students_with_lowest_mark = []
for lowest_count in range(len(CSC4_marks)):
    if CSC4_marks[lowest_count] == lowest:
        students_with_lowest_mark.append(CSC4_names[lowest_count])

print(f"the students with the highest marks are {students_with_highest_mark}")
print(f"the students with the lowest marks are {students_with_lowest_mark}")

print()

#Q7) sort the marks array and accordingly names array in order from highest to lowest marks

#sorted_marks_list = CSC4_marks.sort(reverse=True)

# using bubble sort
for i in range(65):
    for j in range(64):
        if CSC4_marks[j]< CSC4_marks[j+1]:
            tempMarks = CSC4_marks[j]
            CSC4_marks[j] = CSC4_marks[j+1]
            CSC4_marks[j + 1] = tempMarks
            tempNames = CSC4_names[j]
            CSC4_names[j] = CSC4_names[j+1]
            CSC4_names[j+1] = tempNames

print("SORTED")
for count in range(65):
    print(CSC4_names[count], "=" ,CSC4_marks[count])



