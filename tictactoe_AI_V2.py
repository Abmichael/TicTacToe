from random import choice as choose
from random import randint

def displayBoard(board):
    """The Skeleton of the board and displaying of it"""
    print('\n'*20)
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

def playerInput():
    """Take player input and set appropriate variables"""
    Identity1 = ''
    while Identity1.lower() != 'x' and Identity1.lower() != 'o':
        Identity1 = input("Do you want to be X or O: ")
    if Identity1.lower() == "o":
        return ("O","X")
    else:
        return ("X","O")

def play(Identity,board):
    """set the board based on player input"""
    choice=0
    while not 0<choice<=9:
        choice = int(input("\tChoose position(1-9): "))
        try:
            assert 0<choice<=9
        except AssertionError: continue

        if board[choice-1] == ' ':
            board[choice-1]=Identity
        else:
            print('taken!')
            choice=0
    displayBoard(board)

def won(b,Identity):
    """check if the game have been won"""
    #Return true if "any" of the possible combinations is true
    #ACROSS,DIAGONAL,VERTICAL
    return any([b[0]==b[1]==b[2]==Identity,b[3]==b[4]==b[5]==Identity,\
                b[6]==b[7]==b[8]==Identity,b[1]==b[4]==b[7]==Identity,\
                b[2]==b[5]==b[8]==Identity,b[0]==b[3]==b[6]==Identity,\
                b[0]==b[4]==b[8]==Identity,b[2]==b[4]==b[6]==Identity])

def wannaPlay():
    """confirm if player want to play again"""

    confirmation = input('wanna play again?(Y or N) ')
    if confirmation.lower() == 'y':
        return True
    else: 
        return False
    
def isNextWin(board,identity,possibilities):
    """Check if a next move can be a winning move"""
    for i in possibilities:
        copyb = board[:]
        copyb[i]=identity
        if won(copyb,identity):
            return i+1
    else:
        return False

def RandomMov(identity1,identity2,board):
    """The Computer AI Logic"""
    choice = 4
    #list of indices of empty spots,hence a possible moving position
    possibilities = [x for x,y in enumerate(board) if y ==' ']
    corners = [x for x in possibilities if x in [0,2,6,8]]
    #to prevent replacing of already taken spots
    while board[choice].lower() != ' ':

        #to prevent calling the function 4 times,save the result to variables
        #check if The player can win on his next move and block that road!
        #check if we can win on our next move and take that chance
        Pwinning = isNextWin(board,identity1,possibilities)
        
        Cwinning = isNextWin(board,identity2,possibilities)

        if Cwinning:
            choice = Cwinning-1
        elif Pwinning:
            choice = Pwinning-1
        elif corners:
            choice = choose(corners)
        else:
            if possibilities:
                choice = choose(possibilities)

    board[choice]=identity2
    displayBoard(board)

def main():
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    identity1,identity2 = playerInput()
    Turn = randint(1,2)
    displayBoard(board)
    if Turn==1:
        print('Player Goes First!')
    else: print('Computer Goes First!')
    while not (won(board,identity1) or won(board,identity2)):
        if Turn==1:
            print('Player:')
            play(identity1,board)
            if won(board,identity1):
                print('Player won!')
                again = wannaPlay()
            Turn=2
        else:
            print('Computer:')
            RandomMov(identity1,identity2,board)
            if won(board,identity2):
                print('Computer won!')
                again = wannaPlay()
            Turn=1
        draw = all(list(map(lambda x: x != ' ',board)))
        if draw:
            print("Draw!")
            again = wannaPlay()
        try:
            if again:
                board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
                Turn = randint(1,2)
                del again
                displayBoard(board)
            else:
                break
        except NameError:
            pass
        
if __name__=="__main__":
    main()