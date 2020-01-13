
#reate a board
player = "X"
winner = False
board = ['-','-','-',
         '-','-','-',
         '-','-','-']

def play():
    display_board()
    print(player + 's turn')
    player_choice()
    check_for_win()
    flip_player()


#display board
def display_board():
    print(board[0]+' | '+board[1]+' | '+board[2])
    print(board[3]+' | '+board[4]+' | '+board[5])
    print(board[6]+' | '+board[7]+' | '+board[8])

def player_choice():
    global player
    position = 0
#take input from player and display it in board
    position = input("Choose a position from 1-9: ")
    #filter input
    while position not in ['1','2','3','4','5','6','7','8','9']:
            position = input("Invalid position, Choose a position from 1-9: ")
    position = int(position) - 1
    #stop overwritting
    if board[position] == '-':
        board[position] = player
    else:
        print("Already taken")
        player_choice()

#check for win
def check_for_win():
    global winner
    global player
    check_rows()
    check_cols()
    check_diagonals()
    check_tie()
    if winner == True:
        display_board()
        print(player + 'wins')

    #player = "x"

def check_rows():
    global winner
    if board[0] == board[1] == board[2] != '-' or board[3] == board[4] == board[5] != '-' or board[6] == board[7] == board[8] != '-' :
     #   print(player + "wins")
       winner = True


def check_cols():
    global winner
    if board[0] == board[3] == board[6] != '-' or board[1] == board[4] == board[7] != '-' or board[2] == board[5] == board[8] != '-':
      #  print(player + "wins")
         winner = True


def check_diagonals():
    global winner
    if board[0] == board[4] == board[8] != '-' or board[2] == board[4] == board[6] != '-':
       # print(player + "wins")
         winner = True

def check_tie():
    global winner
    if "-" not in board:
        print('Its a tie')
        #winner = True
        quit()




def flip_player():
    global player
    if player == "X":
        player = "0"
    elif player == "0":
        player = "X"


while winner != True:
    play()


'''play() 
    take input and place it in board
    check if win
    check rows
    check cols 
    check diagonals
    if win
    print winner 
check if tie
    if tie print tie    
while check if win is not
     play()
'''