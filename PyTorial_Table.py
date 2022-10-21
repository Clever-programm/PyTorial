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
        MainWindow.resize(960, 540)
        MainWindow.setFixedSize(960, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Mini_main_img = QtWidgets.QLabel(self.centralwidget)
        self.Mini_main_img.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.Mini_main_img.setText("")
        self.Mini_main_img.setPixmap(QtGui.QPixmap("PyTutorial_Table1.png"))
        self.Mini_main_img.setObjectName("Mini_main_img")
        self.Pproger_main_img = QtWidgets.QLabel(self.centralwidget)
        self.Pproger_main_img.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.Pproger_main_img.setText("")
        self.Pproger_main_img.setPixmap(QtGui.QPixmap("PyTutorial_Table2.png"))
        self.Pproger_main_img.setObjectName("Pproger_main_img")
        self.Pproger_main_img.hide()
        self.Courses_main_img = QtWidgets.QLabel(self.centralwidget)
        self.Courses_main_img.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.Courses_main_img.setText("")
        self.Courses_main_img.setPixmap(QtGui.QPixmap("PyTutorial_Table3.png"))
        self.Courses_main_img.setObjectName("Courses_main_img")
        self.Courses_main_img.hide()
        self.Profile_main_img = QtWidgets.QLabel(self.centralwidget)
        self.Profile_main_img.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.Profile_main_img.setText("")
        self.Profile_main_img.setPixmap(QtGui.QPixmap("PyTutorial_Table4.png"))
        self.Profile_main_img.setObjectName("Profile_main_img")
        self.Profile_round_img = QtWidgets.QLabel(self.centralwidget)
        self.Profile_round_img.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.Profile_round_img.setText("")
        self.Profile_round_img.setPixmap(QtGui.QPixmap("PyTutorial_Table4_1.png"))
        self.Profile_round_img.setObjectName("Profile_round_img")
        self.Profile_proround_img = QtWidgets.QLabel(self.centralwidget)
        self.Profile_proround_img.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.Profile_proround_img.setText("")
        self.Profile_proround_img.setPixmap(QtGui.QPixmap("PyTutorial_Table4_2.png"))
        self.Profile_proround_img.setObjectName("Profile_proround_img")
        self.Profile_proround_img.hide()
        self.Profile_choose_img = QtWidgets.QLabel(self.centralwidget)
        self.Profile_choose_img.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.Profile_choose_img.setText("")
        self.Profile_choose_img.setPixmap(QtGui.QPixmap("PyTutorial_Table4_3.png"))
        self.Profile_choose_img.setObjectName("Profile_choose_img")
        self.Mini_wiki_img = QtWidgets.QLabel(self.centralwidget)
        self.Mini_wiki_img.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.Mini_wiki_img.setText("")
        self.Mini_wiki_img.setPixmap(QtGui.QPixmap("PyTutorial_Table1_1.png"))
        self.Mini_wiki_img.setObjectName("Mini_wiki_img")
        self.Courses_first_img = QtWidgets.QLabel(self.centralwidget)
        self.Courses_first_img.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.Courses_first_img.setText("")
        self.Courses_first_img.setPixmap(QtGui.QPixmap("PyTutorial_Table3_1.png"))
        self.Courses_first_img.setObjectName("Courses_first_img")
        self.Courses_first_img.hide()
        self.Courses_second_img = QtWidgets.QLabel(self.centralwidget)
        self.Courses_second_img.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.Courses_second_img.setText("")
        self.Courses_second_img.setPixmap(QtGui.QPixmap("PyTutorial_Table3_2.png"))
        self.Courses_second_img.setObjectName("Courses_second_img")
        self.Courses_second_img.hide()
        self.Profile_photo_img = QtWidgets.QLabel(self.centralwidget)
        self.Profile_photo_img.setGeometry(QtCore.QRect(186, 70, 133, 133))
        self.Profile_photo_img.setText("")
        self.Profile_photo_img.setObjectName("Profile_photo_img")
        self.Mini_photo_img = QtWidgets.QLabel(self.centralwidget)
        self.Mini_photo_img.setGeometry(QtCore.QRect(10, 12, 31, 31))
        self.Mini_photo_img.setText("")
        self.Mini_photo_img.setObjectName("Mini_photo_img")
        self.Profile_nickname_txt = QtWidgets.QLabel(self.centralwidget)
        self.Profile_nickname_txt.setGeometry(QtCore.QRect(370, 70, 500, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Profile_nickname_txt.setFont(font)
        self.Profile_nickname_txt.setObjectName("Profile_nickname_txt")
        self.Profile_CID_txt = ClickedLabel(self.centralwidget)
        self.Profile_CID_txt.setGeometry(QtCore.QRect(370, 100, 500, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Profile_CID_txt.setFont(font)
        self.Profile_CID_txt.setObjectName("Profile_CID_txt")
        self.Profile_CID_txt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Profile_CID_txt.setToolTip('Скопировать в буфер обмена')
        self.Profile_pproger_txt = QtWidgets.QLabel(self.centralwidget)
        self.Profile_pproger_txt.setGeometry(QtCore.QRect(370, 125, 500, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Profile_pproger_txt.setFont(font)
        self.Profile_pproger_txt.setObjectName("Profile_pproger_txt")
        self.Profile_languages_txt = QtWidgets.QLabel(self.centralwidget)
        self.Profile_languages_txt.setGeometry(QtCore.QRect(370, 150, 500, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Profile_languages_txt.setFont(font)
        self.Profile_languages_txt.setObjectName("Profile_languages_txt")
        self.Profile_courses_txt = QtWidgets.QLabel(self.centralwidget)
        self.Profile_courses_txt.setGeometry(QtCore.QRect(370, 175, 500, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Profile_courses_txt.setFont(font)
        self.Profile_courses_txt.setObjectName("Profile_courses_txt")
        self.Mini_wiki_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.Mini_wiki_edit.setGeometry(QtCore.QRect(12, 236, 138, 20))
        self.Mini_wiki_edit.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.Mini_wiki_edit.setFrame(False)
        self.Mini_wiki_edit.setObjectName("Mini_wiki_edit")
        self.Mini_wiki_txt = QtWidgets.QLabel(self.centralwidget)
        self.Mini_wiki_txt.setGeometry(QtCore.QRect(13, 220, 133, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.Mini_wiki_txt.setFont(font)
        self.Mini_wiki_txt.setStyleSheet("color: rgb(255, 255, 255);")
        self.Mini_wiki_txt.setObjectName("Mini_wiki_txt")
        self.Mini_profile_txt = ClickedLabel(self.centralwidget)
        self.Mini_profile_txt.setGeometry(QtCore.QRect(13, 70, 133, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Mini_profile_txt.setFont(font)
        self.Mini_profile_txt.setStyleSheet("color: rgb(255, 255, 255);")
        self.Mini_profile_txt.setObjectName("Mini_profile_txt")
        self.Mini_profile_txt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Mini_courses_txt = ClickedLabel(self.centralwidget)
        self.Mini_courses_txt.setGeometry(QtCore.QRect(13, 95, 133, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Mini_courses_txt.setFont(font)
        self.Mini_courses_txt.setStyleSheet("color: rgb(255, 255, 255);")
        self.Mini_courses_txt.setObjectName("Mini_courses_txt")
        self.Mini_courses_txt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Mini_pproger_txt = ClickedLabel(self.centralwidget)
        self.Mini_pproger_txt.setGeometry(QtCore.QRect(13, 120, 133, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Mini_pproger_txt.setFont(font)
        self.Mini_pproger_txt.setStyleSheet("color: rgb(255, 255, 255);")
        self.Mini_pproger_txt.setObjectName("Mini_pproger_txt")
        self.Mini_pproger_txt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Mini_about_txt = ClickedLabel(self.centralwidget)
        self.Mini_about_txt.setGeometry(QtCore.QRect(13, 145, 133, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Mini_about_txt.setFont(font)
        self.Mini_about_txt.setStyleSheet("color: rgb(255, 255, 255);")
        self.Mini_about_txt.setObjectName("Mini_about_txt")
        self.Mini_about_txt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Mini_nick_txt = QtWidgets.QLabel(self.centralwidget)
        self.Mini_nick_txt.setGeometry(QtCore.QRect(50, 15, 95, 13))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.Mini_nick_txt.setFont(font)
        self.Mini_nick_txt.setStyleSheet("color: rgb(255, 255, 255);")
        self.Mini_nick_txt.setObjectName("Mini_nick_txt")
        self.Mini_CID_txt = QtWidgets.QLabel(self.centralwidget)
        self.Mini_CID_txt.setGeometry(QtCore.QRect(50, 30, 95, 13))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.Mini_CID_txt.setFont(font)
        self.Mini_CID_txt.setStyleSheet("color: rgb(255, 255, 255);")
        self.Mini_CID_txt.setObjectName("Mini_CID_txt")
        self.Profile_choose_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Profile_choose_btn.setGeometry(QtCore.QRect(186, 217, 136, 22))
        self.Profile_choose_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Profile_choose_btn.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.Profile_choose_btn.setText("")
        self.Profile_choose_btn.setObjectName("Profile_choose_btn")
        self.Courses_first_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Courses_first_btn.setGeometry(QtCore.QRect(182, 70, 273, 181))
        self.Courses_first_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Courses_first_btn.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.Courses_first_btn.setText("")
        self.Courses_first_btn.setObjectName("Courses_first_btn")
        self.Courses_first_btn.hide()
        self.Courses_second_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Courses_second_btn.setGeometry(QtCore.QRect(182, 269, 273, 181))
        self.Courses_second_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Courses_second_btn.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.Courses_second_btn.setText("")
        self.Courses_second_btn.setObjectName("Courses_second_btn")
        self.Courses_second_btn.hide()
        self.Mini_photo_img.raise_()
        self.Mini_main_img.raise_()
        self.Mini_wiki_img.raise_()
        self.Mini_wiki_txt.raise_()
        self.Mini_nick_txt.raise_()
        self.Mini_CID_txt.raise_()
        self.Profile_photo_img.raise_()
        self.Profile_main_img.raise_()
        self.Profile_round_img.raise_()
        self.Profile_proround_img.raise_()
        self.Profile_choose_img.raise_()
        self.Profile_nickname_txt.raise_()
        self.Profile_CID_txt.raise_()
        self.Profile_pproger_txt.raise_()
        self.Profile_languages_txt.raise_()
        self.Profile_courses_txt.raise_()
        self.Profile_choose_btn.raise_()
        self.Courses_main_img.raise_()
        self.Courses_first_img.raise_()
        self.Courses_second_img.raise_()
        self.Courses_first_btn.raise_()
        self.Courses_second_btn.raise_()
        self.Pproger_main_img.raise_()
        self.Mini_profile_txt.raise_()
        self.Mini_courses_txt.raise_()
        self.Mini_pproger_txt.raise_()
        self.Mini_about_txt.raise_()
        self.Mini_wiki_edit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyTorial"))
        self.Profile_nickname_txt.setText(_translate("MainWindow", "Nickname(3-20 letters)"))
        self.Profile_CID_txt.setText(_translate("MainWindow", "CID: #000000"))
        self.Profile_pproger_txt.setText(_translate("MainWindow", "P-proger: off"))
        self.Profile_languages_txt.setText(_translate("MainWindow", "Языки: None"))
        self.Profile_courses_txt.setText(_translate("MainWindow", "Курсов пройдено: 0"))
        self.Mini_wiki_txt.setText(_translate("MainWindow", "Поиск по Википедии"))
        self.Mini_profile_txt.setText(_translate("MainWindow", "Профиль"))
        self.Mini_courses_txt.setText(_translate("MainWindow", "Курсы"))
        self.Mini_pproger_txt.setText(_translate("MainWindow", "P-proger"))
        self.Mini_about_txt.setText(_translate("MainWindow", "О приложении"))
        self.Mini_nick_txt.setText(_translate("MainWindow", "Nickname(3-20 letters)"))
        self.Mini_CID_txt.setText(_translate("MainWindow", "CID: #000000"))