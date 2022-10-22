# импортируем необходимые библиотеки
import sqlite3
import pyrebase
import sys
import pyperclip as pclip
from PIL import Image
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
# импортируем Свои_Окна
from PyTorial_Main import Ui_MainWindow as Main_Window
from PyTorial_Reg import Ui_MainWindow as Reg_Window
from PyTorial_Table import Ui_MainWindow as Table_Window


# окно ошибки
def error_box(msg):
    error = QMessageBox()
    error.setWindowTitle('Ошибка')
    error.setText(msg)
    error.setIcon(QMessageBox.Warning)
    error.exec()


# классы ошибок
class DataExcept(Exception):
    pass


class PassExcept(Exception):
    pass


class NickExcept(Exception):
    pass


class EmailExcept(Exception):
    pass


class DBExcept(Exception):
    pass


class UserExcept(Exception):
    pass


# класс Главного_Окна (ГОТОВО!!!)
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
        email = self.Edit_email.text()
        password = self.Edit_password.text()
        con = sqlite3.connect('BDsql.db')
        cur = con.cursor()
        try:
            if not (email and password):
                raise DataExcept
            # поиск по базе данных
            CID = int(list(cur.execute(f"""SELECT CID FROM PyUsers
                                           WHERE Email = '{email}'
                                           AND Password = '{password}'"""))[0][0])
            if CID:
                self.table = TableWidget(CID)
                self.table.show()
                self.close()
            else:
                raise UserExcept
        except DataExcept:
            error_box('Заполните все поля!')
        except UserExcept:
            error_box('Такого пользователя не существует!')
        except Exception as e:
            error_box('Произошла непредвиденная ошибка')
            print(e)
        finally:
            if con:
                con.close()


# класс Окна_Регистрации (ГОТОВО!!!)
class RegWidget(QMainWindow, Reg_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.regist.clicked.connect(self.register)

    def register(self):
        nick = self.Edit_nickname.text()
        email = self.Edit_email.text()
        pas1 = self.Edit_password.text()
        pas2 = self.Edit_password_2.text()
        con = sqlite3.connect('BDsql.db')
        cur = con.cursor()
        try:
            # проверка введённых данных
            if not (nick and email and pas1 and pas2):
                raise DataExcept
            if not (3 <= len(nick) <= 20):
                raise NickExcept
            if email.find('@gmail.com') == -1 and \
                    email.find('@yandex.ru') == -1 and \
                    email.find('@mail.ru') == -1:
                raise EmailExcept
            if pas1 != pas2:
                raise PassExcept
            if list(cur.execute(f"""SELECT * FROM PyUsers 
                               WHERE Email = '{email}'""")):
                raise DBExcept
            # добавление пользователя к базе данных
            cur.execute(f"""INSERT INTO PyUsers (Nickname, Email, Password) 
                            VALUES ('{nick}', '{email}', '{pas1}')""")
            con.commit()
            # переход к Рабочему_Окну
            CID = int(list(cur.execute(f"""SELECT CID FROM PyUsers
                                           WHERE Email = '{email}'
                                           AND Password = '{pas1}'"""))[0][0])
            if CID:
                self.table = TableWidget(CID)
                self.table.show()
                self.close()
            else:
                raise Exception
        except DataExcept:
            error_box('Заполните все поля!')
        except NickExcept:
            error_box("Никнейм должен содержать 3-20 символов!")
        except EmailExcept:
            error_box('Некорректный адрес электронной почты!\n(@gmail.com, @yandex.ru, @mail.ru)')
        except PassExcept:
            error_box("Пароли не совпадают!")
        except DBExcept:
            error_box(f'Пользователь с почтой {email} уже существует!')
        except Exception as e:
            error_box('Произошла непредвиденная ошибка')
            print(e)
        finally:
            if con:
                con.close()


# класс Рабочего_Окна (новые вкладки, работа бд с имг)
class TableWidget(QMainWindow, Table_Window):
    def __init__(self, CID):
        super().__init__()
        self.setupUi(self)
        self.CID = CID
        self.Nick = None
        self.Avatar = None
        self.Pproger = False
        self.Courses = 0
        # инициализация базы данных
        con = sqlite3.connect('BDsql.db')
        cur = con.cursor()
        self.Nick, self.Avtar, self.Pproger, self.Courses = list(cur.execute(f"""
                SELECT Nickname, Avatar, Pproger, Courses FROM PyUsers
                WHERE CID = {self.CID}
        """))[0]
        try:
            pass
        except Exception as e:
            error_box('Произошла непредвиденная ошибка')
            print(e)
            self.main = MainWidget()
            self.main.show()
            self.close()
        finally:
            if con:
                con.close()
        # необходимые преобразования
        self.Profile_CID_txt.setText('CID: #' + str(self.convert_base(self.CID, to_base=16)).rjust(6, '0'))
        self.Profile_nickname_txt.setText(self.Nick)
        self.Profile_pproger_txt.setText('P-proger: ' + self.Pproger * 'on' + int(not bool(self.Pproger)) * 'off')
        self.Profile_courses_txt.setText('Курсов пройдено: ' + str(self.Courses))
        if self.Pproger:
            self.Profile_proround_img.show()
        self.Mini_CID_txt.setText('CID: #' + str(self.convert_base(self.CID, to_base=16)).rjust(6, '0'))
        self.Mini_nick_txt.setText(self.Nick)
        # кнопки
        self.Profile_CID_txt.clicked.connect(self.copy)
        self.Mini_profile_txt.clicked.connect(self.choose_profile)
        self.Mini_courses_txt.clicked.connect(self.choose_courses)
        self.Mini_pproger_txt.clicked.connect(self.choose_pproger)
        self.Mini_about_txt.clicked.connect(self.choose_about)
        self.Profile_choose_btn.clicked.connect(self.choose_avatar)

    def convert_base(self, num, to_base=10, from_base=10):
        if isinstance(num, str):
            n = int(num, from_base)
        else:
            n = int(num)
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n < to_base:
            return alphabet[n]
        else:
            return self.convert_base(n // to_base, to_base) + alphabet[n % to_base]

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
        mini_img_size = 31
        try:
            avatar_d = QFileDialog.getOpenFileName(self, "Open file", 'C:', 'JPG File (*.jpg);;PNG File (*.png)')
            avatar = Image.open(avatar_d[0])
            form = avatar_d[1]
            # корректировка изображения
            if avatar.size[0] > avatar.size[1]:
                delta = img_size / float(avatar.size[1])
                delta_mini = mini_img_size / float(avatar.size[1])
                x = int(float(avatar.size[0]) * delta)
                y = int(float(avatar.size[1]) * delta)
                x_mini = int(float(avatar.size[0]) * delta_mini)
                y_mini = int(float(avatar.size[1]) * delta_mini)
                cropy = ((x - 133) // 2, 0, (x - 133) // 2 + 133, 133)
                cropy_mini = ((x_mini - 31) // 2, 0, (x_mini - 31) // 2 + 31, 31)
                avatar = avatar.resize((x, y)).crop(cropy)
                avatar_mini = avatar.resize((x_mini, y_mini)).crop(cropy_mini)
            else:
                delta = img_size / float(avatar.size[0])
                delta_mini = mini_img_size / float(avatar.size[0])
                x = int(float(avatar.size[0]) * delta)
                y = int(float(avatar.size[1]) * delta)
                x_mini = int(float(avatar.size[0]) * delta_mini)
                y_mini = int(float(avatar.size[1]) * delta_mini)
                cropy = (0, (y - 133) // 2, 133, (y - 133) // 2 + 133)
                cropy_mini = (0, (y_mini - 31) // 2, 31, (y_mini - 31) // 2 + 31)
                avatar = avatar.resize((x, y)).crop(cropy)
                avatar_mini = avatar.resize((x_mini, y_mini)).crop(cropy_mini)
            # сохранение и установка аватарки
            avatar.save('avatar.jpg')
            self.Profile_photo_img.setPixmap(QtGui.QPixmap('avatar.jpg'))
            avatar_mini.save('avatar_mini.jpg')
            self.Mini_photo_img.setPixmap(QtGui.QPixmap('avatar_mini.jpg'))
        except BaseException as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWidget()
    main.show()
    sys.exit(app.exec_())
