#SYNTAX FOR 2D ARRAYS
# <array name> = [[<initial val> for col in range(<range for col>)] for row in range(<range for row>)]
#ROW IS ALWAYS OUTER LOOP
#COL IS ALWAYS INNER LOOP

board = [[0 for col in range(7)] for row in range(6)]
print("\nboard") #\n is for skipping each consecutive line when printing
for row in range(6):
    for col in range(7):
        print(board[row][col], end = "")
    print()

print()

#<array name> [row][col]
board2 = [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]]
board2[1][5] = 5
for row in range(6):
    for col in range(7):
        print(board2[row][col], end=" ")
        print()
