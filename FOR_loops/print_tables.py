#Q1 Ask a user for a number and print its multiplication table(1-10)

mainNum = int(input("Enter a number for its table: "))
for multiplier in range(1,11):
    ans = mainNum * multiplier
    print(mainNum, "*", multiplier, "=", ans)
