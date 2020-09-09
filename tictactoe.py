from random import randint

def dispaly_board(board):
    """The Skeleton of the board and displaying of it"""
    print('\n'*20)
    #board=[1,2,3
    #       4,5,6
    #       7,8,9]
    print('''
                 |     | 
              {0}  |  {1}  |  {2}
            _____|_____|_____
                 |     | 
              {3}  |  {4}  |  {5}
            _____|_____|_____
                 |     | 
              {6}  |  {7}  |  {8}
                 |     |

                        '''.format(*board))

def player_input():
    """Take player input and set appropriate variables"""
    Identity1 = ''
    while Identity1.lower() != 'x' and Identity1.lower() != 'o':
        Identity1 = input("Do you want to be X or O: ")
    if Identity1.lower() == "o":
        Identity1 = Identity1.upper()
        Identity2 = "X"
    else:
        Identity1 = "X"
        Identity2 = "O"
    return (Identity1,Identity2)

def play(Identity,board):
    """set the board based on player input"""
    newboard = board
    choice=10
    while not 0<choice<=9:
        choice = int(input("\tChoose position(1-9): "))
        try:
            assert 0<choice<=9, '1-9 allowed'
        except AssertionError: continue
        if newboard[choice-1].lower() == ' ':
            newboard[choice-1]=Identity
        else:
            print('taken!')
            choice=10
    dispaly_board(newboard)
    return newboard

def won(bo):
    """check if the game have been won"""
    b=bo[:]
    for i in range(len(b)):
        if b[i] == ' ':
            b[i]=str(i)
    return any([b[0]==b[1]==b[2],b[3]==b[4]==b[5],\
                b[6]==b[7]==b[8],b[1]==b[4]==b[7],\
                b[2]==b[5]==b[8],b[0]==b[3]==b[6],\
                b[0]==b[4]==b[8],b[2]==b[4]==b[6]])

def wannaPlay():
    confirmation = input('wanna play again?(Y or N) ')
    if confirmation.lower() == 'y':
        global board
        board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        global Turn
        Turn = 2
    else: return

def main():
    global board
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    identity1,identity2 = player_input()
    global Turn
    Turn=2
    dispaly_board(board)
    if Turn==1:
        print('Player 1 Goes First!')
    else: print('Player 2 Goes First')
    draw = all(list(map(lambda x: x != ' ',board)))
    while not won(board):
        if Turn==1:
            print('Player 1:')
            play(identity1,board)
            if won(board):
                print('Player 1 won!')
                wannaPlay()
            Turn=2
        else:
            print('Player 2:')
            play(identity2,board)
            if won(board):
                print('Player 2 won!')
                wannaPlay()
            Turn=1
        draw = all(list(map(lambda x: x != ' ',board)))
        if not won(board) and draw:
            print("Draw!")
            wannaPlay()
            break
        
        
if __name__=="__main__":
    main()