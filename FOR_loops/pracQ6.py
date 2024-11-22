#Q6 make a 2 player rock,paper,scissor game that runs for n rounds, ask user for n value. output winner of each round and game

p1score = 0
p2score = 0

n = int(input("how many rounds do you want to play?:"))
print()

for rounds in range(1,n+1):
    p1move = input("Player 1, select your move (r,p,s):")
    p2move = input("Player 2, select your move (r,p,s):")
    print()

    while (p1move != "r" and p1move != "s" and p1move != "p") or (p2move != "r" and p2move != "s" and p2move != "p"):
        print("wrong move! Try again")
        print()
        p1move = input("Player 1, select your move (r,p,s):")
        p2move = input("Player 2, select your move (r,p,s):")
        print()

    if p1move == p2move:
        print("* Round drawn :/ *")
        print()
    elif (p1move =='r' and p2move == 's') or (p1move =='s' and p2move == 'p') or (p1move =='p' and p2move == 'r'):
            p1score +=1
            print("* Player 1 wins the round! *")
            print()
    else:
            p2score +=1
            print("* Player 2 wins the round! *")
            print()

if p1score == p2score:
    print("* The game was a draw *")
elif p1score > p2score:
    print("* Player 1 has won the game! =D * ")
else:
    print("* Player 2 has won the game! =D *")