import rsa
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit, QScrollArea

class MainWindow(QMainWindow):
    # 0 = Alice
    # 1 = Mike
    # 2 = Greg
    users = [None, None, None]
    currentPushed = None
    message = None
    encryptedMessage = None

    def __init__(self):
        super().__init__()
        self.setWindowTitle("RSA Key Generator")
        self.setGeometry(100, 100, 800, 600)

        mainLayout = QHBoxLayout()
        leftLayout = QVBoxLayout()
        rightLayout = QVBoxLayout()

        NamesLayout = QVBoxLayout()
        NamesLayout.addStretch()
        NamesLayout.addWidget(QLabel("Select a user to send message to:"))

        self.standardBtnStylesheet = """
        QPushButton {
            background-color: lightgray;
        }
        QPushButton:hover {
            background-color: gray;
        }
        QPushButton:pressed {
            background-color: darkgray;
        }
        """

        self.activeBtnStylesheet = """
        QPushButton {
            background-color: lightblue;
        }
        QPushButton:hover {
            background-color: blue;
        }
        QPushButton:pressed {
            background-color: darkblue;
        }
        """

        self.aliceBtn = QPushButton("Alice")
        self.aliceBtn.setStyleSheet(self.standardBtnStylesheet)
        self.aliceBtn.clicked.connect(lambda: self.selectUser(0))
        NamesLayout.addWidget(self.aliceBtn)

        self.mikeBtn = QPushButton("Mike")
        self.mikeBtn.setStyleSheet(self.standardBtnStylesheet)
        self.mikeBtn.clicked.connect(lambda: self.selectUser(1))
        NamesLayout.addWidget(self.mikeBtn)

        self.gregBtn = QPushButton("Greg")
        self.gregBtn.setStyleSheet(self.standardBtnStylesheet)
        self.gregBtn.clicked.connect(lambda: self.selectUser(2))
        NamesLayout.addWidget(self.gregBtn)

        NamesLayout.addStretch()
        leftLayout.addLayout(NamesLayout)

        initializationLayout = QVBoxLayout()
        initializationScroll = QScrollArea()
        initializationScroll.setWidgetResizable(True)
        self.initializationMessage = QVBoxLayout()
        content_widget = QWidget()
        content_widget.setLayout(self.initializationMessage)
        initializationScroll.setWidget(content_widget)
        initializationLayout.addWidget(initializationScroll)
        rightLayout.addLayout(initializationLayout)
        messagesLayout = QVBoxLayout()
        self.messagesScroll = QScrollArea()
        self.messagesScroll.setWidgetResizable(True)
        self.messages = QVBoxLayout()
        self.messages.setSpacing(0)
        message_wdiget = QWidget()
        message_wdiget.setLayout(self.messages)
        self.messagesScroll.setWidget(message_wdiget)
        messagesLayout.addWidget(self.messagesScroll)
        bottomMessage = QHBoxLayout()
        self.messageInput = QLineEdit()
        self.messageInput.returnPressed.connect(lambda: self.sendMessage(self.currentPushed))
        self.messegeSendBtn = QPushButton("Send")
        self.messegeSendBtn.clicked.connect(lambda: self.sendMessage(self.currentPushed))
        bottomMessage.addWidget(self.messageInput)
        bottomMessage.addWidget(self.messegeSendBtn)
        messagesLayout.addLayout(bottomMessage)

        rightLayout.addLayout(messagesLayout)
        rightLayout.addWidget(self.messageInput)

        mainLayout.addLayout(leftLayout)
        mainLayout.addLayout(rightLayout)

        mainWidget = QWidget()
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

        mainLayout.setStretch(0, 2)
        mainLayout.setStretch(1, 8)
    
    def selectUser(self, user):
        if user == 0 and self.currentPushed != 0:
            self.aliceBtn.setStyleSheet(self.activeBtnStylesheet)
            self.mikeBtn.setStyleSheet(self.standardBtnStylesheet)
            self.gregBtn.setStyleSheet(self.standardBtnStylesheet)
            if(self.users[0] == None):
                self.users[0] = rsa.rsa()
            self.initProcess(0)
            self.removeContent(self.messages)
            self.currentPushed = 0
        elif user == 1 and self.currentPushed != 1:
            self.aliceBtn.setStyleSheet(self.standardBtnStylesheet)
            self.mikeBtn.setStyleSheet(self.activeBtnStylesheet)
            self.gregBtn.setStyleSheet(self.standardBtnStylesheet)
            if(self.users[1] == None):
                self.users[1] = rsa.rsa()
            self.initProcess(1)
            self.removeContent(self.messages)
            self.currentPushed = 1
        elif user == 2 and self.currentPushed != 2:
            self.aliceBtn.setStyleSheet(self.standardBtnStylesheet)
            self.mikeBtn.setStyleSheet(self.standardBtnStylesheet)
            self.gregBtn.setStyleSheet(self.activeBtnStylesheet)
            if(self.users[2] == None):
                self.users[2] = rsa.rsa()
            self.initProcess(2)
            self.removeContent(self.messages)
            self.currentPushed = 2
        self.messageInput.setFocus()

    def initProcess(self, user):
        if user == 0:
            self.removeContent(self.initializationMessage)
            self.initializationMessage.addWidget(QLabel("Step 1: p and q\np:" + str(self.users[0].p) + "\nq:" + str(self.users[0].q)))
            self.initializationMessage.addWidget(QLabel("Step 2: n\nn:" + str(self.users[0].n)))
            self.initializationMessage.addWidget(QLabel("Step 3: phi\nphi:" + str(self.users[0].phi)))
            self.initializationMessage.addWidget(QLabel("Step 4: e by gcd(e, phi) = 1\ne:" + str(self.users[0].e)))
            self.initializationMessage.addWidget(QLabel("Step 5: d by mod_inverse(e, phi)\nd:" + str(self.users[0].d)))
            self.initializationMessage.addWidget(QLabel("Public Key: (" + str(self.users[0].public_key[0])))
        elif user == 1:
            self.removeContent(self.initializationMessage)
            self.initializationMessage.addWidget(QLabel("Step 1: p and q\np:" + str(self.users[1].p) + "\nq:" + str(self.users[1].q)))
            self.initializationMessage.addWidget(QLabel("Step 2: n\nn:" + str(self.users[1].n)))
            self.initializationMessage.addWidget(QLabel("Step 3: phi\nphi:" + str(self.users[1].phi)))
            self.initializationMessage.addWidget(QLabel("Step 4: e by gcd(e, phi) = 1\ne:" + str(self.users[1].e)))
            self.initializationMessage.addWidget(QLabel("Step 5: d by mod_inverse(e, phi)\nd:" + str(self.users[1].d)))
            self.initializationMessage.addWidget(QLabel("Public Key: (" + str(self.users[1].public_key[0])))
        elif user == 2:
            self.removeContent(self.initializationMessage)
            self.initializationMessage.addWidget(QLabel("Step 1: p and q\np:" + str(self.users[2].p) + "\nq:" + str(self.users[2].q)))
            self.initializationMessage.addWidget(QLabel("Step 2: n\nn:" + str(self.users[2].n)))
            self.initializationMessage.addWidget(QLabel("Step 3: phi\nphi:" + str(self.users[2].phi)))
            self.initializationMessage.addWidget(QLabel("Step 4: e by gcd(e, phi) = 1\ne:" + str(self.users[2].e)))
            self.initializationMessage.addWidget(QLabel("Step 5: d by mod_inverse(e, phi)\nd:" + str(self.users[2].d)))
            self.initializationMessage.addWidget(QLabel("Public Key: (" + str(self.users[2].public_key[0])))

    def removeContent(self, layout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)

    def sendMessage(self, user):
        if user == 0:
            self.encryptedMessage = self.users[0].encrypt(self.messageInput.text())
            self.messages.addWidget(QLabel("Encrypted: "))
            for i in self.encryptedMessage:
                self.messages.addWidget(QLabel(str(i)))
            self.message = self.users[0].decrypt(self.encryptedMessage)
            self.messages.addWidget(QLabel("Decrypted: " + self.message + "\n"))
        elif user == 1:
            self.encryptedMessage = self.users[1].encrypt(self.messageInput.text())
            self.messages.addWidget(QLabel("Encrypted: "))
            for i in self.encryptedMessage:
                self.messages.addWidget(QLabel(str(i)))
            self.message = self.users[1].decrypt(self.encryptedMessage)
            self.messages.addWidget(QLabel("Decrypted: " + self.message + "\n"))
        elif user == 2:
            self.encryptedMessage = self.users[2].encrypt(self.messageInput.text())
            self.messages.addWidget(QLabel("Encrypted: "))
            for i in self.encryptedMessage:
                self.messages.addWidget(QLabel(str(i)))
            self.message = self.users[2].decrypt(self.encryptedMessage)
            self.messages.addWidget(QLabel("Decrypted: " + self.message + "\n"))
        else:
            self.removeContent(self.messages)
            self.messages.addWidget(QLabel("Please select a user to send message to."))
        self.messageInput.clear()
        self.messageInput.setFocus()
        QTimer.singleShot(200,  lambda: self.messagesScroll.verticalScrollBar().setValue(self.messagesScroll.verticalScrollBar().maximum()))