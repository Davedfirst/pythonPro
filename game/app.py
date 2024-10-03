board=["  "for i in range(9)]


def display_board():
    row="|{}|{}|{}|".format(board[0], board[1], board[2])
    row1="|{}|{}|{}|".format(board[3], board[4], board[5])
    row2="|{}|{}|{}|".format(board[6], board[7], board[8])

    print()
    print(row)
    print(row1)
    print(row2)
    print()


def move(play):
    if play =="X":
        number=1
    elif play =="O":
        number = 2
    print("Your turn player {}".format(number))
    choice = int(input("Enter moves from (1-9): ").strip())
    if board[choice-1]=="  ":
        board[choice-1]= play
    else:
        print()
        print("move already played")

def win(play):
    if (board[0]==play and board[1]==play and board[2]==play) or\
       (board[3]==play and board[4]==play and board[5]==play) or\
       (board[6]==play and board[7]==play and board[8]==play) or\
       (board[0]==play and board[3]==play and board[6]==play) or\
       (board[1]==play and board[4]==play and board[7]==play) or\
       (board[2]==play and board[5]==play and board[8]==play) or\
       (board[0]==play and board[4]==play and board[8]==play) or\
       (board[2]==play and board[4]==play and board[6]==play):
        return True
    else:
        return False
def draw():
    if "  " not in board:
        return True
    else:
        return False
while True:
    display_board()
    move("X")
    display_board()
    if win("X"):
        print("X wins this round")
        break
    elif draw():
        print("it's a draw")
        break
    move("O")
    display_board()
    if win("O"):
        print("O wins this round")
        break
    elif draw():
        print("it's a draw")
        break
            
