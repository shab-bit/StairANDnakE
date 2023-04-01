from PyQt6 import QtCore, QtGui, QtWidgets
from random import randint


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(689, 781)
        Form.setMinimumSize(QtCore.QSize(689, 781))
        Form.setMaximumSize(QtCore.QSize(689, 781))
        Form.setStyleSheet("background-color : #2C3E50;")
        self.tass = QtWidgets.QPushButton(parent=Form)
        self.tass.setGeometry(QtCore.QRect(10, 270, 121, 500))
        self.tass.setMinimumSize(QtCore.QSize(0, 500))
        font = QtGui.QFont()
        font.setFamily("Jokerman")
        font.setPointSize(36)
        self.tass.setFont(font)
        self.tass.setStyleSheet("background-color:#D0D3D4;")
        self.tass.setObjectName("tass")
        self.soccer = QtWidgets.QLabel(parent=Form)
        self.soccer.setGeometry(QtCore.QRect(10, 10, 121, 71))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(22)
        self.soccer.setFont(font)
        self.soccer.setStyleSheet("background-color:#58D68D;\n"
"border-radius : 10px ;")
        self.soccer.setObjectName("soccer")
        self.reset = QtWidgets.QPushButton(parent=Form)
        self.reset.setGeometry(QtCore.QRect(10, 197, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(24)
        self.reset.setFont(font)
        self.reset.setStyleSheet("background-color:white ;")
        self.reset.setObjectName("reset")
        self.time = QtWidgets.QLCDNumber(parent=Form)
        self.time.setGeometry(QtCore.QRect(-30, 90, 161, 91))
        self.time.setStyleSheet("background-color:#F1948A ;border-radius : 10px ;")
        self.time.setObjectName("time")
        self.zamin = QtWidgets.QLabel(parent=Form)
        self.zamin.setGeometry(QtCore.QRect(170, 30, 481, 721))
        self.zamin.setStyleSheet("background-image : url(./snake.jpg);")
        self.zamin.setText("")
        self.zamin.setObjectName("zamin")
        self.mohre1 = QtWidgets.QLabel(parent=Form)
        self.mohre1.setGeometry(QtCore.QRect(60, 580, 281, 231))
        font = QtGui.QFont()
        font.setFamily("PhrasticMedium")
        font.setPointSize(36)
        self.mohre1.setFont(font)
        self.mohre1.setStyleSheet("border-image: url(./mohre2.png);\n"
"background : none ;")
        self.mohre1.setText("")
        self.mohre1.setObjectName("mohre1")
        self.mohre2 = QtWidgets.QLabel(parent=Form)
        self.mohre2.setGeometry(QtCore.QRect(50, 600, 281, 231))
        font = QtGui.QFont()
        font.setFamily("PhrasticMedium")
        font.setPointSize(36)
        self.mohre2.setFont(font)
        self.mohre2.setStyleSheet("border-image: url(./mohre1.png);\n"
"background : none ;")
        self.mohre2.setText("")
        self.mohre2.setObjectName("mohre2")

        self.xp = 0 
        self.po_now = 1
        self.po_old = 1
        self.jahat = 1
        self.po_now1 = 1
        self.po_old1 = 1
    
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tass.setText(_translate("Form", "tass"))
        self.soccer.setText(_translate("Form", ":)"))
        self.reset.setText(_translate("Form", "reset"))
        self.tass.clicked.connect(self.tasser)
        self.reset.clicked.connect(self.reseter)

        
        
        

    def reseter(self):
        self.tass.setStyleSheet("background-color:#D0D3D4;")
        self.mohre1.setGeometry(QtCore.QRect(60, 580, 281, 231))
        self.mohre2.setGeometry(QtCore.QRect(50, 600, 281, 231))
        self.xp = 0 
        self.po_now = 1
        self.po_old = 1
        self.po_now1 = 1
        self.po_old1 = 1
        self.jahat = 1
        
        
    def tasser(self):
        time = QtCore.QTime.currentTime()
        text = time.toString('hh:mm:ss')
        self.time.display(text)
        self.po_now += randint(1,6)
        print("now|||>", self.po_now)
        if self.po_now > 96 :
                self.po_now = self.po_old
        else:
                while self.po_now > self.po_old :
                        
                        print(self.po_old)
                        
                        if not(self.po_old % 8) :
                                self.mohre1.setGeometry(QtCore.QRect(self.mohre1.x(), self.mohre1.y() - 58, 281, 231))
                        
                        elif int((self.po_old / 8 ) % 2) :
                                self.mohre1.setGeometry(QtCore.QRect(self.mohre1.x() - 60, self.mohre1.y(), 281, 231))
                        
                        else :
                                self.mohre1.setGeometry(QtCore.QRect(self.mohre1.x() + 60, self.mohre1.y(), 281, 231))
                        
                        self.xp += 1
                        self.soccer.setText(str(self.xp))
                        self.po_old += 1
                
                if self.po_now in [39 , 51 ,59 ,77 ,86 ,94] :
                        war = {39:5 , 51:34 ,59:38 ,77:52 ,86:61 ,94:48}
                        self.po_old = war[self.po_old]
                        self.po_now = self.po_old
                        if int(self.po_now / 8)%2 :
                                self.mohre1.setGeometry(QtCore.QRect(60 + (60*(8-(int(self.po_now % 8)))),580-(58*int(self.po_now / 8)), 281, 231))
                        else :
                                self.mohre1.setGeometry(QtCore.QRect(60 + (60*int(self.po_now % 8)),580-(58*int(self.po_now / 8)), 281, 231))
                        
                        
                elif self.po_now in [3,10,18,35,73 ,78]:
                        good = {3:19,10:42,18:47,35:60,73:89 ,78:82}
                        self.po_old = good[self.po_old]
                        self.po_now = self.po_old
                        if int(self.po_now / 8)%2 :
                                self.mohre1.setGeometry(QtCore.QRect(60 + (60*(8-(int(self.po_now % 8)))),580-(58*int(self.po_now / 8)), 281, 231))
                        else :
                                self.mohre1.setGeometry(QtCore.QRect(60 + (60*int(self.po_now % 8)),580-(58*int(self.po_now / 8)), 281, 231))
                        
                        
                elif self.po_now == 96 :
                        self.tass.setStyleSheet("background-color:green;")
                        
                        
        #####
        self.po_now1 += randint(1,6)
        print("now|||>", self.po_now1)
        if self.po_now1 > 96 :
                self.po_now1 = self.po_old1
        else:
                while self.po_now1 > self.po_old1 :
                        
                        print(self.po_old1)
                        
                        if not(self.po_old1 % 8) :
                                self.mohre2.setGeometry(QtCore.QRect(self.mohre2.x(), self.mohre2.y() - 58, 281, 231))
                        
                        elif int((self.po_old1 / 8 ) % 2) :
                                self.mohre2.setGeometry(QtCore.QRect(self.mohre2.x() - 60, self.mohre2.y(), 281, 231))
                        
                        else :
                                self.mohre2.setGeometry(QtCore.QRect(self.mohre2.x() + 60, self.mohre2.y(), 281, 231))
                        
                        self.soccer.setText(str(self.xp))
                        self.po_old1 += 1
                
                
                if self.po_now1 in [39 , 51 ,59 ,77 ,86 ,94] :
                        war = {39:5 , 51:34 ,59:38 ,77:52 ,86:61 ,94:48}
                        self.po_old1 = war[self.po_old1]
                        self.po_now1 = self.po_old1
                        if int(self.po_now1 / 8)%2 :
                                self.mohre2.setGeometry(QtCore.QRect(60 + (60*(8-(int(self.po_now1 % 8)))),580-(58*int(self.po_now1 / 8)), 281, 231))
                        else :
                                self.mohre2.setGeometry(QtCore.QRect(60 + (60*int(self.po_now1 % 8)),580-(58*int(self.po_now1 / 8)), 281, 231))
                        
                        
                elif self.po_now1 in [3,10,18,35,73 ,78]:
                        good = {3:19,10:42,18:47,35:60,73:89 ,78:82}
                        self.po_old1 = good[self.po_old1]
                        self.po_now1 = self.po_old1
                        if int(self.po_now1 / 8)%2 :
                                self.mohre2.setGeometry(QtCore.QRect(60 + (60*(8-(int(self.po_now1 % 8)))),580-(58*int(self.po_now1 / 8)), 281, 231))
                        else :
                                self.mohre2.setGeometry(QtCore.QRect(60 + (60*int(self.po_now1 % 8)),580-(58*int(self.po_now1 / 8)), 281, 231))
                        
                        
                elif self.po_now1 == 96 :
                        self.tass.setStyleSheet("background-color:red;")                
        
                        
                        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
