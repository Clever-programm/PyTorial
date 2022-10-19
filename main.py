# импортируем необходимые библиотеки
import sys
import sqlite3 as sql
import pyperclip as pclip
from PIL import Image
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
# импортируем Свои_Окна
from PyTorial_Main import Ui_MainWindow as Main_Window
from PyTorial_Reg import Ui_MainWindow as Reg_Window
from PyTorial_Table import Ui_MainWindow as Table_Window


# класс Главного_Окна
class MainWidget(QMainWindow, Main_Window):
    # инициализация Главного_Окна
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # кнопки
        self.sign_out.clicked.connect(self.go_reg)
        self.sign_in.clicked.connect(self.go_table)

    # переход к Окну_Регистрации
    def go_reg(self):
        try:
            self.reg = RegWidget()
            self.reg.show()
            self.close()
        except Exception as e:
            print(e)

    # переход к Рабочему_Окну
    def go_table(self):
        try:
            self.table = TableWidget()
            self.table.show()
            self.close()
        except Exception as e:
            print(e)


# класс Окна_Регистрации
class RegWidget(QMainWindow, Reg_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


# класс Рабочего_Окна
class TableWidget(QMainWindow, Table_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # кнопки
        self.Profile_CID_txt.clicked.connect(self.copy)
        self.Mini_profile_txt.clicked.connect(self.choose_profile)
        self.Mini_courses_txt.clicked.connect(self.choose_courses)
        self.Mini_pproger_txt.clicked.connect(self.choose_pproger)
        self.Mini_about_txt.clicked.connect(self.choose_about)
        self.Profile_choose_btn.clicked.connect(self.choose_avatar)

    def copy(self):
        pclip.copy(self.Profile_CID_txt.text()[6:])

    def choose_profile(self):
        self.Profile_main_img.show()
        self.Courses_main_img.hide()
        self.Courses_second_img.hide()
        self.Courses_first_img.hide()
        self.Courses_second_btn.hide()
        self.Courses_first_btn.hide()
        self.Pproger_main_img.hide()

    def choose_courses(self):
        self.Profile_main_img.hide()
        self.Courses_main_img.show()
        self.Courses_second_img.show()
        self.Courses_first_img.show()
        self.Courses_second_btn.show()
        self.Courses_first_btn.show()
        self.Pproger_main_img.hide()

    def choose_pproger(self):
        self.Profile_main_img.hide()
        self.Courses_main_img.hide()
        self.Courses_second_img.hide()
        self.Courses_first_img.hide()
        self.Courses_second_btn.hide()
        self.Courses_first_btn.hide()
        self.Pproger_main_img.show()

    def choose_about(self):
        pass

    def choose_avatar(self):
        img_size = 133
        try:
            avatar_d = QFileDialog.getOpenFileName(self, "Open file", 'C:', 'JPG File (*.jpg);;PNG File (*.png)')
            avatar = Image.open(avatar_d[0])
            if avatar.size[0] > avatar.size[1]:
                delta = img_size / float(avatar.size[1])
            else:
                delta = img_size / float(avatar.size[0])
            x = int(float(avatar.size[0]) * delta)
            y = int(float(avatar.size[1]) * delta)
            avatar = avatar.resize((x, y))
            avatar.save('avatar.jpg')
            self.Profile_photo_img.setPixmap(QtGui.QPixmap('avatar.jpg'))
        except BaseException as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWidget()
    main.show()
    sys.exit(app.exec_())
