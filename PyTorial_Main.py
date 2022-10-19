from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        MainWindow.setFixedSize(960, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainImage = QtWidgets.QLabel(self.centralwidget)
        self.MainImage.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.MainImage.setText("")
        self.MainImage.setPixmap(QtGui.QPixmap("PyTutorial_Project_Main1.jpg"))
        self.MainImage.setObjectName("MainImage")
        self.RegImage = QtWidgets.QLabel(self.centralwidget)
        self.RegImage.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.RegImage.setText("")
        self.RegImage.setPixmap(QtGui.QPixmap("PyTutorial_Project_Main2.png"))
        self.RegImage.setObjectName("RegImage")
        self.sign_in = QtWidgets.QPushButton(self.centralwidget)
        self.sign_in.setGeometry(QtCore.QRect(631, 380, 255, 30))
        self.sign_in.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sign_in.setAutoFillBackground(False)
        self.sign_in.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.sign_in.setText("")
        self.sign_in.setObjectName("Sign_in")
        self.sign_out = QtWidgets.QPushButton(self.centralwidget)
        self.sign_out.setGeometry(QtCore.QRect(631, 422, 255, 30))
        self.sign_out.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sign_out.setAutoFillBackground(False)
        self.sign_out.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.sign_out.setText("")
        self.sign_out.setObjectName("Sign_out")
        self.Edit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.Edit_email.setGeometry(QtCore.QRect(641, 166, 235, 15))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.Edit_email.setFont(font)
        self.Edit_email.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.Edit_email.setFrame(False)
        self.Edit_email.setInputMask("")
        self.Edit_email.setText("")
        self.Edit_email.setObjectName("Edit_email")
        self.Edit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.Edit_password.setGeometry(QtCore.QRect(641, 202, 235, 15))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.Edit_password.setFont(font)
        self.Edit_password.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.Edit_password.setFrame(False)
        self.Edit_password.setInputMask("")
        self.Edit_password.setText("")
        self.Edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Edit_password.setObjectName("Edit_password")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyTorial"))
        self.Edit_email.setPlaceholderText(_translate("MainWindow", "E-mail"))
        self.Edit_password.setPlaceholderText(_translate("MainWindow", "Password"))
