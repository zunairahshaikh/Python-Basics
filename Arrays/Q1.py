#Q1 make a 2d array to store sales of 5 salespersons' sales for 12 months
salesOfTheYear = [[0 for months in range(2)] for person in range(5)]
for person in range(5):
    for months in range(2):
        print(salesOfTheYear[person][months], end = "")
    print()

#Q2 ask user to enter sales of each sales person
for person in range(5):
    for months in range(2):
        saleOfMonth = input(f"enter the sales of month {months+1}: ")
        salesOfTheYear[person][months] = saleOfMonth
print(salesOfTheYear, end = "")

print()

#Q3 calc the avg sales for each salesperson and average sales of all salespersons
overall_sum = 0
for person in range(5):
    for months in range(2):
        overall_sum = overall_sum + int(salesOfTheYear[person][months])
        overall_avg_sales = overall_sum/len(salesOfTheYear)
print(f"the average sales of all the salespeople is {overall_avg_sales}")

