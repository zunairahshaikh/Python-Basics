
#Q6) create a tic tac toe board
def displayBoard(board):  #create the board
    for row in range(3):
        for col in range(3):
            print(board[row][col], end=" ")
        print()

def BoardInput(board,userSymbol):  #function to take input of the user and validate it
    userRow = int(input('enter row number: '))-1
    userCol = int(input('enter column number: '))-1
    while board[userRow][userCol] != '-':
        print("space already filled")
        print()
        userRow = int(input('enter row number: '))-1
        userCol = int(input('enter column number: '))-1
    board[userRow][userCol] = userSymbol
    return board

def boardCheck(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] !='-':
            return True, board[i][0]
        if board[0][i] == board[1][i] ==  board[2][i] and board[0][i] !='-':
            return True, board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != "-":
        return True, board[1][1]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return True, board[1][1]
    return False, '-'

board = [["-" for col in range(3)]for row in range(3)]
playerSymbol = ['X','O']
playerNum = 0
moves = 0
win = False
while win == False:
    displayBoard(board)
    print("turn for player ", playerNum+1)
    board = BoardInput(board, playerSymbol[playerNum])
    moves += 1
    win, winSymbol = boardCheck(board)
    playerNum = (playerNum+1)%2
displayBoard(board)
if win == True:
    print(winSymbol, " wins the game")
else:
    print("the game is a draw")
