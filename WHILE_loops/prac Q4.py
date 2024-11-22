#Q keep asking a user for numbers until user enters a zero
#for all even numbers entered add them to the total
#for all odd numbers entered subtract them to the total
#for all prime numbers multiply them w/ the total

total = 0

usernum = int(input("ayoooo enter a number: "))

while usernum != 0:
  if usernum % 2 == 0:
      total += usernum
  else:
      total -= usernum
  isPrime = True
  for i in range(2,usernum):
      if usernum % i ==0:
          isPrime = False
  if isPrime:
      total *= usernum

print(f"your total is {total}")