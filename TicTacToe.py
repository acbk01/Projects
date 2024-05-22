from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, QLineEdit, QPushButton)



playFlag = 0
playerX = 0
playerO = 0
Turn = 0


class CrossandCircle(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        global Name1
        global Name2
        
        Name1 = QLineEdit(self)
        Name1.text() == " "
        Name2 = QLineEdit(self)
        Name2.text() == " "
        
        global Player1
        global Player2
        
        Player1 = QPushButton(self)
        Player1.setEnabled(False)
        Player2 = QPushButton(self)
        Player2.setEnabled(False)
        
        self.title = "Menu"
        self.resize(600, 600)
        
        self.StartBtn = QPushButton("Start", self)
        self.StartBtn.setGeometry(0, 0, 600, 300)
        self.UstawieniaBtn = QPushButton("Ustawienia", self)
        self.UstawieniaBtn.setGeometry(0, 300, 600, 300)
                
        self.StartBtn.clicked.connect(self.game)
        self.UstawieniaBtn.clicked.connect(self.settings)
        
        self.main_window()
        
    def main_window(self):
        self.setWindowTitle(self.title)
        self.show()                        
        
    def game(self):
        self.w = Game()
        self.w.show()
        self.hide()
    
    def settings(self):
        self.w = Settings()
        self.w.show()
        self.hide()
        
    
    
class Settings(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Ustawienia")
        self.resize(600, 600)
        
        self.etykieta1 = QLabel("Nazwa gracza 1:", self)
        self.etykieta1.move(250, 150)
        self.etykieta2 = QLabel("Nazwa gracza 2:", self)
        self.etykieta2.move(250, 330)
        
        global Name1
        global Name2
        
        Name1 = QLineEdit(self)
        Name1.move(245, 190)
        Name2 = QLineEdit(self)
        Name2.move(245, 360)
        
        self.Starter = QLabel("Rozpoczyna gracz:", self)
        self.Starter.move(250, 420)
        
        global Player1
        global Player2
        
        Player1 = QPushButton("1", self)
        Player1.clicked.connect(self.click1)
        Player1.resize(20, 20)
        Player1.move(260, 450)
        Player2 = QPushButton("2", self)
        Player2.clicked.connect(self.click2)
        Player2.resize(20, 20)
        Player2.move(310, 450)
        
        self.ZapiszBtn = QPushButton("Zapisz i rozpocznij rozgrywkę", self)
        self.ZapiszBtn.move(170, 500)
        self.ZapiszBtn.resize(250, 50)
        self.ZapiszBtn.clicked.connect(self.game)


    def click1(self):
        Player1.setEnabled(False)
        Player2.setEnabled(True)
        
    def click2(self):
        Player2.setEnabled(False)
        Player1.setEnabled(True)
                               
    def game(self):
        self.w = Game()
        self.w.show()
        self.hide()
        

 
class Draw(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Remis")
        self.resize(200, 50)       
        self.draw = QLabel("Gracze zremisowali!", self)
        self.draw.move(50, 10)
        self.draw.resize(100, 30)
        
class WinnerX(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Zwycięzca")
        self.resize(200, 50)    
        
        if Name1.text() != Name2.text():
            self.XWon = QLabel("Gracz " + Name1.text() + " wygrał!", self)
            self.XWon.move(50, 10)
            self.XWon.resize(130, 30)
        
        else:
            self.XWon = QLabel("Gracz 1 wygrał!", self)
            self.XWon.move(50, 10)
            self.XWon.resize(100, 30)
        
class WinnerO(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Zwycięzca")
        self.resize(200, 50)     
        
        if Name1.text() != Name2.text():
            self.OWon = QLabel("Gracz " + Name2.text() + " wygrał!", self)
            self.OWon.move(50, 10)
            self.OWon.resize(130, 30)
            
        else:
            self.OWon = QLabel("Gracz 2 wygrał!", self)
            self.OWon.move(50, 10)
            self.OWon.resize(100, 30)
        

class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Gra")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(180, 50, 411, 421))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")



        self.p1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p1.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.p1.setFont(font)
        self.p1.setText("")
        self.p1.setObjectName("p1")
        self.gridLayout.addWidget(self.p1, 0, 0, 1, 1)
        self.p1.clicked.connect(lambda: self.btnClk(1))



        self.p2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p2.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.p2.setFont(font)
        self.p2.setText("")
        self.p2.setObjectName("p2")
        self.gridLayout.addWidget(self.p2, 0, 1, 1, 1)
        self.p2.clicked.connect(lambda: self.btnClk(2))


        self.p5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p5.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.p5.setFont(font)
        self.p5.setText("")
        self.p5.setObjectName("p5")
        self.gridLayout.addWidget(self.p5, 1, 1, 1, 1)
        self.p5.clicked.connect(lambda: self.btnClk(5))


        self.p6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p6.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.p6.setFont(font)
        self.p6.setText("")
        self.p6.setObjectName("p6")
        self.gridLayout.addWidget(self.p6, 1, 2, 1, 1)
        self.p6.clicked.connect(lambda: self.btnClk(6))


        self.p4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p4.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.p4.setFont(font)
        self.p4.setText("")
        self.p4.setObjectName("p4")
        self.gridLayout.addWidget(self.p4, 1, 0, 1, 1)
        self.p4.clicked.connect(lambda: self.btnClk(4))


        self.p3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p3.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.p3.setFont(font)
        self.p3.setText("")
        self.p3.setObjectName("p3")
        self.gridLayout.addWidget(self.p3, 0, 2, 1, 1)
        self.p3.clicked.connect(lambda: self.btnClk(3))


        self.p7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p7.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.p7.setFont(font)
        self.p7.setText("")
        self.p7.setObjectName("p7")
        self.gridLayout.addWidget(self.p7, 2, 0, 1, 1)
        self.p7.clicked.connect(lambda: self.btnClk(7))


        self.p8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p8.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.p8.setFont(font)
        self.p8.setText("")
        self.p8.setObjectName("p8")
        self.gridLayout.addWidget(self.p8, 2, 1, 1, 1)
        self.p8.clicked.connect(lambda: self.btnClk(8))


        self.p9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p9.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.p9.setFont(font)
        self.p9.setText("")
        self.p9.setObjectName("p9")
        self.gridLayout.addWidget(self.p9, 2, 2, 1, 1)
        self.p9.clicked.connect(lambda: self.btnClk(9))
        
        
        if Name1.text() != Name2.text():
            self.Xscore = QLabel("Wynik gracza " + Name1.text(), self)
            self.Xscore.move(60, 475)
            self.Xscore.resize(150,20)
            self.WynikX = QtWidgets.QLabel(self.centralwidget)
            self.WynikX.setGeometry(QtCore.QRect(90, 485, 101, 41))
            self.WynikX.setObjectName("WynikX")
            self.Yscore = QLabel("Wynik gracza " + Name2.text(), self)
            self.Yscore.move(530, 475)
            self.Yscore.resize(150,20)
            self.WynikO = QtWidgets.QLabel(self.centralwidget)
            self.WynikO.setGeometry(QtCore.QRect(560, 495, 101, 31))
            self.WynikO.setObjectName("WynikO")
            self.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(self)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
            self.menubar.setObjectName("menubar")
            self.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(self)
            self.statusbar.setObjectName("statusbar")
            self.setStatusBar(self.statusbar)
            
            self.Turn1 = QLabel("Ruch gracza " + Name1.text(), self)
            self.Turn1.move(350, 10)
            self.Turn1.resize(150, 50)
            self.Turn2 = QLabel("Ruch gracza " + Name2.text(), self)
            self.Turn2.move(350, 10)
            self.Turn2.resize(150, 50)
            
            if Player1.isEnabled() == Player2.isEnabled() or Player2.isEnabled():
                self.Turn1.setVisible(True)
                self.Turn2.setVisible(False)
                
            elif Player1.isEnabled():
                self.Turn1.setVisible(False)
                self.Turn2.setVisible(True)
                
        else:            
            self.Xscore = QLabel("Wynik gracza 1", self)            
            self.Xscore.move(60, 475)
            self.Xscore.resize(150,20)
            self.WynikX = QtWidgets.QLabel(self.centralwidget)
            self.WynikX.setGeometry(QtCore.QRect(90, 485, 101, 41))
            self.WynikX.setObjectName("WynikX")
            self.Yscore = QLabel("Wynik gracza 2", self)
            self.Yscore.move(530, 475)
            self.Yscore.resize(150,20)
            self.WynikO = QtWidgets.QLabel(self.centralwidget)
            self.WynikO.setGeometry(QtCore.QRect(560, 495, 101, 31))
            self.WynikO.setObjectName("WynikO")
            self.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(self)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
            self.menubar.setObjectName("menubar")
            self.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(self)
            self.statusbar.setObjectName("statusbar")
            self.setStatusBar(self.statusbar)
            
            self.Turn1 = QLabel("Ruch gracza 1", self)
            self.Turn1.move(350, 10)
            self.Turn1.resize(100, 50)
            self.Turn2 = QLabel("Ruch gracza 2", self)
            self.Turn2.move(350, 10)
            self.Turn2.resize(100, 50)
            
            if Player1.isEnabled() == Player2.isEnabled() or Player2.isEnabled():
                self.Turn1.setVisible(True)
                self.Turn2.setVisible(False)
                
            elif Player1.isEnabled():
                self.Turn1.setVisible(False)
                self.Turn2.setVisible(True)
            
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)        
        
        
    def resetBoard(self):
        self.p1.setEnabled(True)
        self.p1.setText(' ')
        self.p2.setEnabled(True)
        self.p2.setText(' ')
        self.p3.setEnabled(True)
        self.p3.setText(' ')
        self.p4.setEnabled(True)
        self.p4.setText(' ')
        self.p5.setEnabled(True)
        self.p5.setText(' ')
        self.p6.setEnabled(True)
        self.p6.setText(' ')
        self.p7.setEnabled(True)
        self.p7.setText(' ')
        self.p8.setEnabled(True)
        self.p8.setText(' ')
        self.p9.setEnabled(True)
        self.p9.setText(' ')

    def btnClk(self, pos):
        
        global playFlag
        mark = ''
        
        
        if Player1.isEnabled() == Player2.isEnabled() or Player2.isEnabled():
            if(playFlag%2 == 0):
                mark = 'X'
                self.Turn1.setVisible(False)
                self.Turn2.setVisible(True)

    
            else:
                mark = 'O'
                self.Turn1.setVisible(True)
                self.Turn2.setVisible(False)
                
            if pos == 1:
                self.p1.setText(mark)
                self.p1.setEnabled(False)                
    
            if pos == 2:
                self.p2.setText(mark)
                self.p2.setEnabled(False)
    
            if pos == 3:
                self.p3.setText(mark)
                self.p3.setEnabled(False)
    
            if pos == 4:
                self.p4.setText(mark)
                self.p4.setEnabled(False)
    
            if pos == 5:
                self.p5.setText(mark)
                self.p5.setEnabled(False)
    
            if pos == 6:
                self.p6.setText(mark)
                self.p6.setEnabled(False)
    
            if pos == 7:
                self.p7.setText(mark)
                self.p7.setEnabled(False)
    
            if pos == 8:
                self.p8.setText(mark)
                self.p8.setEnabled(False)
    
            if pos == 9:
                self.p9.setText(mark)
                self.p9.setEnabled(False)
    
            playFlag += 1
            self.chkWin()
        
        
        elif Player1.isEnabled():
            if(playFlag%2 == 1):
                mark = 'X'
                self.Turn1.setVisible(False)
                self.Turn2.setVisible(True)
    
    
            else:
                mark = 'O'    
                self.Turn1.setVisible(True)
                self.Turn2.setVisible(False)
    
            if pos == 1:
                self.p1.setText(mark)
                self.p1.setEnabled(False)
    
            if pos == 2:
                self.p2.setText(mark)
                self.p2.setEnabled(False)
    
            if pos == 3:
                self.p3.setText(mark)
                self.p3.setEnabled(False)
    
            if pos == 4:
                self.p4.setText(mark)
                self.p4.setEnabled(False)
    
            if pos == 5:
                self.p5.setText(mark)
                self.p5.setEnabled(False)
    
            if pos == 6:
                self.p6.setText(mark)
                self.p6.setEnabled(False)
    
            if pos == 7:
                self.p7.setText(mark)
                self.p7.setEnabled(False)
    
            if pos == 8:
                self.p8.setText(mark)
                self.p8.setEnabled(False)
    
            if pos == 9:
                self.p9.setText(mark)
                self.p9.setEnabled(False)
    
            playFlag += 1
            self.chkWin()
        
        
        


    def chkWin(self):
        global playerO
        global playerX
        winner = ''


        if self.p1.text() == self.p2.text() and self.p2.text() == self.p3.text():
            winner = self.p1.text()
            
            

        elif self.p1.text() == self.p4.text() and self.p4.text() == self.p7.text():
            winner = self.p1.text()
            
            

        elif self.p2.text() == self.p5.text() and self.p5.text() == self.p8.text():
            winner = self.p2.text()
            
           

        elif self.p3.text() == self.p6.text() and self.p6.text() == self.p9.text():
            winner = self.p3.text()
            
        

        elif self.p7.text() == self.p5.text() and self.p5.text() == self.p3.text():
            winner = self.p7.text()
            
           

        elif self.p4.text() == self.p5.text() and self.p5.text() == self.p6.text():
            winner = self.p4.text()
            
           

        elif self.p7.text() == self.p8.text() and self.p8.text() == self.p9.text():
            winner = self.p7.text()
            
            

        elif self.p1.text() == self.p5.text() and self.p5.text() == self.p9.text():
            winner = self.p1.text()
            
            
        elif self.p1.isEnabled() == self.p2.isEnabled() == self.p3.isEnabled() == self.p4.isEnabled() == self.p5.isEnabled() == self.p6.isEnabled() == self.p7.isEnabled() == self.p8.isEnabled() == self.p9.isEnabled():
            self.w = Draw()
            self.w.show()
            self.resetBoard()
                    
        if winner == 'X':
            playerX += 1
            self.WynikX.setText(str(playerX))
            self.resetBoard()
    
            self.w = WinnerX()
            self.w.show()
            
        if winner == 'O':
            playerO += 1
            self.WynikO.setText(str(playerO))
            self.resetBoard()
            
            self.w = WinnerO()
            self.w.show()        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.WynikX.setText(_translate("MainWindow", " "))
        self.WynikO.setText(_translate("MainWindow", " "))
        
        
        
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = CrossandCircle()
    sys.exit(app.exec_())

