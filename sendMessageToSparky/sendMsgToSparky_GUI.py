'''
Installazione su Ubuntu/Debian
sudo apt install pyqt5-dev python3-pyqt5 python3-pyqt5.qtwebengine
'''

# importo librerie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

import sendMsgToSparky

class myGUI():
    def __init__(self):
        self.app = QApplication([])
        # crea una finestra
        self.window = QWidget()
        self.sender = sendMsgToSparky.sendMsgToSparky()
        self.initUI()


    def initUI(self):
        self.window.resize(500, 500)
        self.window.setWindowTitle('SignoSoftware - Send Msg to Sparky Bot')
        # main vertical layout
        self.layoutVert = QVBoxLayout()

        # horizontal layouts
        self.layoutHorizEmail = QHBoxLayout()
        self.layoutHorizMessage = QHBoxLayout()
        self.layoutHorizButtons = QHBoxLayout()

        # email
        self.emailLabel = QLabel("Email")
        self.emailText = QLineEdit('')
        self.layoutHorizEmail.addWidget(self.emailLabel)
        self.layoutHorizEmail.addWidget(self.emailText)

        # message
        self.messageLabel = QLabel("Message")
        self.messageText = QTextEdit('')
        self.layoutHorizMessage.addWidget(self.messageLabel)
        self.layoutHorizMessage.addWidget(self.messageText)

        # buttons
        self.buttonSend = QPushButton('Send')
        self.buttonClose = QPushButton('Close')

        # aggiungo bottoni al layout verticale
        self.layoutHorizButtons.addWidget(self.buttonSend)
        self.layoutHorizButtons.addWidget(self.buttonClose)

        self.layoutVert.addLayout(self.layoutHorizEmail)
        self.layoutVert.addLayout(self.layoutHorizMessage)
        self.layoutVert.addLayout(self.layoutHorizButtons)

        # imposto il layout della finestra
        self.window.setLayout(self.layoutVert)

        # definisco le callback
        self.buttonSend.clicked.connect(self.buttonSendCallback)
        self.buttonClose.clicked.connect(self.app.quit)

        # show
        self.window.show()

    def run(self):
        self.app.exec_()

    def buttonSendCallback(self):
        print("Clicked Send Button")
        #textedit.setText("Ciao")
        #self.messageText.append("Ciao")
        self.sender.send(self.messageText.toPlainText())



# ---- BEGIN ------
# inizializzo la GUI
if __name__ == '__main__':
    p = myGUI()
    p.run()