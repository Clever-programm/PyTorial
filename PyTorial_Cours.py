from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel


class ClickedLabel(QLabel):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)

        self.clicked.emit()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 540)
        MainWindow.setFixedSize(980, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # scroll Main
        self.Main_img = QtWidgets.QLabel(self.centralwidget)
        self.Main_img.setGeometry(QtCore.QRect(0, 0, 980, 540))
        self.Main_img.setText("")
        self.Main_img.setPixmap(QtGui.QPixmap("Data/Images/PyTutorial_Courses_1.png"))
        self.Main_img.setObjectName("Main_img")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 980, 540))
        self.scrollArea.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidget = QtWidgets.QWidget()
        self.scrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 980, 540))
        self.scrollAreaWidget.setObjectName("scrollAreaWidget")
        self.layoutScrollMain = QtWidgets.QVBoxLayout()

        # scroll Lesson
        self.Lesson_img = QtWidgets.QLabel(self.centralwidget)
        self.Lesson_img.setGeometry(QtCore.QRect(0, 0, 980, 540))
        self.Lesson_img.setText('')
        self.Lesson_img.setPixmap(QtGui.QPixmap('Data/Images/PyTutorial_Courses_4.png'))
        self.Lesson_img.setObjectName('Lesson_img')
        self.Lesson_img.hide()
        self.scrollAreaLesson = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaLesson.setGeometry(QtCore.QRect(0, 0, 980, 540))
        self.scrollAreaLesson.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.scrollAreaLesson.setWidgetResizable(True)
        self.scrollAreaLesson.setObjectName("scrollAreaLesson")
        self.layoutScroll = QtWidgets.QVBoxLayout()
        self.layoutScroll.addStretch(0)
        self.Lesson_txt = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Lesson_txt.setFont(font)
        self.Lesson_txt.setStyleSheet("color: rgb(255, 255, 255);")
        self.Lesson_txt.setObjectName('Lesson_txt')
        self.layoutButtons = QtWidgets.QHBoxLayout()
        self.layoutButtons.setGeometry(QtCore.QRect(0, 0, 980, 30))
        self.layoutButtons.addStretch(0)
        self.buttons = QtWidgets.QWidget()
        self.rollBack_btn = ClickedLabel()
        self.rollBack_btn.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.rollBack_btn.setText('')
        self.rollBack_btn.setPixmap(QtGui.QPixmap('Data/Images/PyTutorial_Courses_5.png'))
        self.rollBack_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rollBack_btn.setObjectName('rollBack_btn')
        self.layoutButtons.addWidget(self.rollBack_btn)
        self.rollNext_btn = ClickedLabel()
        self.rollNext_btn.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.rollNext_btn.setText('')
        self.rollNext_btn.setPixmap(QtGui.QPixmap('Data/Images/PyTutorial_Courses_6.png'))
        self.rollNext_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rollNext_btn.setObjectName('rollNext_btn')
        self.layoutButtons.addWidget(self.rollNext_btn)
        self.buttons.setLayout(self.layoutButtons)
        self.editProgram = QtWidgets.QTextEdit()
        self.editProgram.setGeometry(QtCore.QRect(0, 0, 900, 500))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.editProgram.setFont(font)
        self.editProgram.setStyleSheet('background-color: rgb(255, 255, 255);')
        self.editProgram.setObjectName('editProgram')
        self.editProgram.setFixedSize(900, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editProgram.sizePolicy().hasHeightForWidth())
        self.editProgram.setSizePolicy(sizePolicy)
        self.editProgram.hide()
        self.layoutResult = QtWidgets.QHBoxLayout()
        self.layoutResult.setGeometry(QtCore.QRect(0, 0, 980, 30))
        self.layoutResult.addStretch(0)
        self.results = QtWidgets.QWidget()
        self.check_btn = ClickedLabel()
        self.check_btn.setGeometry(QtCore.QRect(0, 0, 150, 30))
        self.check_btn.setText('')
        self.check_btn.setPixmap(QtGui.QPixmap('Data/Images/PyTutorial_Courses_7.png'))
        self.check_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_btn.setObjectName('check_btn')
        self.layoutResult.addWidget(self.check_btn)
        self.error_btn = ClickedLabel()
        self.error_btn.setGeometry(QtCore.QRect(0, 0, 150, 30))
        self.error_btn.setText('')
        self.error_btn.setPixmap(QtGui.QPixmap('Data/Images/PyTutorial_Courses_8_0.png'))
        self.error_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.error_btn.setObjectName('error_btn')
        self.layoutResult.addWidget(self.error_btn)
        self.results.setLayout(self.layoutResult)
        self.results.hide()
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 980, 540))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.layoutScroll.addWidget(self.Lesson_txt)
        self.layoutScroll.addWidget(self.editProgram)
        self.layoutScroll.addWidget(self.results)
        self.layoutScroll.addWidget(self.buttons)
        self.scrollAreaWidgetContents.setLayout(self.layoutScroll)
        self.scrollAreaLesson.setWidget(self.scrollAreaWidgetContents)
        self.scrollAreaLesson.hide()
        self.Up_img = QtWidgets.QLabel(self.centralwidget)
        self.Up_img.setGeometry(QtCore.QRect(0, 0, 980, 89))
        self.Up_img.setText("")
        self.Up_img.setPixmap(QtGui.QPixmap("Data/Images/PyTutorial_Courses_2.png"))
        self.Up_img.setObjectName("Up_img")
        self.Name_txt = QtWidgets.QLabel(self.centralwidget)
        self.Name_txt.setGeometry(QtCore.QRect(30, 17, 600, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Name_txt.setFont(font)
        self.Name_txt.setObjectName("Name_txt")
        self.Back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Back_btn.setGeometry(QtCore.QRect(830, 17, 117, 33))
        self.Back_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Back_btn.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.Back_btn.setText("")
        self.Back_btn.setObjectName("Back_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyTorial"))
        self.Name_txt.setText(_translate("MainWindow", "Course_name"))
