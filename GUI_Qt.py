from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import choice as choose
from random import randint
import sys


class Palette(QPushButton):
    """Holder for the XO images"""
    def __init__(self, identity):
        super().__init__()
        self.setFixedSize(QSize(100, 100))
        self.setIconSize(QSize(100,100))


class DialogQ(QDialog):
    
    def __init__(self,winner):
        super(DialogQ, self).__init__()
        self.setWindowTitle("Game Over")
        self.setWindowIcon(QIcon("Assets/icon.png"))

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        if winner != "Draw":
            label = QLabel(winner+" won! Do you want to play again?")
            label.setFont(QFont("Arial",10,840))
        else:
            label = QLabel("It's a Draw! Do you want to play again?")
            label.setFont(QFont("Arial",10,140))

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.setFont(QFont("Arial",10))
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(label)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class TicTacToe(QMainWindow):
    """main window to rule them all"""

    def __init__(self, *args, **kwargs):
        super(TicTacToe, self).__init__(*args, **kwargs)
        self.setWindowTitle("TicTacToe")
        self.setFixedSize(400,450)
        self.setWindowIcon(QIcon("Assets/icon.png"))
        self.player = "x"
        self.computer = "o"
        self.turn = "x"
        self.board = [' ']*9
        self.possibilities = [x for x,y in enumerate(self.board) if y ==' ']

        central = QWidget()
        tictactoe = QLabel("TicTacToe")
        tictactoe.setStyleSheet("font: bold 52px Arial; color: red;")
        tictactoe.setAlignment(Qt.AlignHCenter)
        self.buttons = QButtonGroup()
        page = QVBoxLayout()
        self.gridholder = QGridLayout()

        central.setLayout(page)
        page.addWidget(tictactoe)
        page.addLayout(self.gridholder)
        self.buttons.buttonClicked.connect(self.set_icon)
        self.buttons.buttonClicked[int].connect(self.set_board)
        


        self.set_grid()
        self.gridholder.setContentsMargins(50,31,50,31)
        self.setCentralWidget(central)
        self.setStatusBar(QStatusBar(self))

    def set_grid(self):
        k=0
        for i in range(3):
            for j in range(3):
                but = Palette("")
                self.buttons.addButton(but,k+j)
                self.gridholder.addWidget(but,i,j)
            k+=3

    def get_turn(self):
        if self.turn == "x":
            self.turn = "o"
            return "x"
        elif self.turn == "o":
            self.turn = "x"
            return "o"

    def set_icon(self,but):
        if but.icon().isNull():
            but.setIcon(QIcon("Assets/{}.png".format(self.get_turn())))
            if self.possibilities and not self.won(self.board,self.player):
                self.RandomMov()
            if c:=self.won(self.board,self.player):
                self.onMyToolBarButtonClick("You")
            elif p:=self.won(self.board,self.computer):
                self.onMyToolBarButtonClick("Computer")
            elif not self.possibilities:
                self.onMyToolBarButtonClick("Draw")

    def set_board(self,id):
        self.board[id]=self.turn
        self.possibilities = [x for x,y in enumerate(self.board) if y ==' ']
        
    def won(self,b,Identity):
        """check if the game has been won"""
        #Return true if "any" of the possible combinations is true
        #ACROSS,DIAGONAL,VERTICAL
        return any([b[0]==b[1]==b[2]==Identity,b[3]==b[4]==b[5]==Identity,\
                    b[6]==b[7]==b[8]==Identity,b[1]==b[4]==b[7]==Identity,\
                    b[2]==b[5]==b[8]==Identity,b[0]==b[3]==b[6]==Identity,\
                    b[0]==b[4]==b[8]==Identity,b[2]==b[4]==b[6]==Identity])

    def isNextWin(self,identity):
        """Check if a move can be a winning move"""
        for i in self.possibilities:
            copyb = self.board[:]
            copyb[i]=identity
            if self.won(copyb,identity):
                return i+1
        else:
            return False

    def RandomMov(self):
        """The Computer AI Logic"""
        choice = 4
        corners = [x for x in self.possibilities if x in [0,2,6,8]]
        non_corners = [x for x in self.possibilities if x not in [0,2,6,8]]
        #to prevent replacing of already taken spots
        while self.board[choice].lower() != ' ':

            #to prevent calling the function 4 times,save the result to variables
            #check if The player can win on his next move and block that road!
            #check if we can win on our next move and take that chance
            Pwinning = self.isNextWin(self.player)
            
            Cwinning = self.isNextWin(self.computer)

            if Cwinning:
                choice = Cwinning-1
            elif Pwinning:
                choice = Pwinning-1
            elif corners:
                if self.board[4]==self.computer and len(corners)<3:
                    choice = choose(non_corners)
                else:
                    choice = choose(corners)
            elif self.possibilities:
                choice = choose(self.possibilities)
            # else:
            #     choice = 10

        self.board[choice]=self.computer
        self.possibilities = [x for x,y in enumerate(self.board) if y ==' ']
        self.buttons.button(choice).setIcon(QIcon("Assets/{}.png".format(self.get_turn())))

    def onMyToolBarButtonClick(self, winner):
        dlg = DialogQ(winner)#making it a subset blocks any action on the main window.(called "Modal window")
        
        if dlg.exec_():
            self.resetit()
        else:
            sys.exit()
    
    def resetit(self):
        for button in self.buttons.buttons():
            button.setIcon(QIcon())
        self.player = "x"
        self.computer = "o"
        self.turn = "x"
        self.board = [' ']*9
        self.possibilities = [x for x,y in enumerate(self.board) if y ==' ']

app = QApplication(sys.argv)
window = TicTacToe()
window.show()  # windows are hidden by Default

app.exec_()


