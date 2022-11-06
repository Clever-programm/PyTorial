# импортируем необходимые библиотеки
import sys
import pyperclip as pclip
import wikipedia
from PIL import Image
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
from pathlib import Path
from base64 import b64encode, b64decode
from io import BytesIO
# импортируем Свои_Окна
from PyTorial_Main import Ui_MainWindow as Main_Window
from PyTorial_Reg import Ui_MainWindow as Reg_Window
from PyTorial_Table import Ui_MainWindow as Table_Window
from PyTorial_Cours import Ui_MainWindow as Cours_Window, ClickedLabel
from UserProgram import check as up
# импортируем базу данных
import FireBaseHelper as fbh
from FireBaseHelper import ConnectionExcept

wikipedia.set_lang('ru')


# окно ошибки
def error_box(msg):
    error = QMessageBox()
    error.setWindowTitle('Ошибка')
    error.setText(msg)
    error.setIcon(QMessageBox.Warning)
    error.exec()


# окно вики
def wiki_box(word):
    wiki = QMessageBox()
    wiki.setWindowTitle(word)
    try:
        wiki.setText(wikipedia.summary(word, sentences=2))
    except Exception as e:
        wiki.setText('Информация по данному слову не найдена')
        print(f'WIKI/38: {e}')
    wiki.exec()


# окно ошибки ученика
def program_error_box(text):
    error = QMessageBox()
    error.setWindowTitle('Program error')
    error.setText(text)
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
            print(f'GOREG/80: {e}')

    # переход к Рабочему_Окну
    def go_table(self):
        email = self.Edit_email.text()
        password = self.Edit_password.text()
        try:
            if not (email and password):
                raise DataExcept
            # поиск по базе данных
            data = fbh.check_user_sign(email, password)
            if data:
                self.table = TableWidget(data[1])
                self.table.show()
                self.close()
            else:
                raise PassExcept
        except DataExcept:
            error_box('Заполните все поля!')
        except fbh.UserExcept:
            error_box('Такого пользователя не существует!')
        except PassExcept:
            error_box('Неверный пароль!')
        except ConnectionExcept:
            error_box('Ошибка подключения!')
        except Exception as e:
            error_box('Произошла непредвиденная ошибка')
            print(f'GOTABLE/105: {e}')


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
            if fbh.find_user_by_email(email):
                raise DBExcept
            fbh.new_user(nick, email, pas1)
            # переход к Рабочему_Окну
            data = fbh.check_user_sign(email, pas1)
            self.table = TableWidget(data[1])
            self.table.show()
            self.close()
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
        except ConnectionExcept:
            error_box('Ошибка подключения!')
        except Exception as e:
            error_box('Произошла непредвиденная ошибка')
            print(f'REGISTER/152: {e}')


# класс Рабочего_Окна (по возможности музыка)
class TableWidget(QMainWindow, Table_Window):
    def __init__(self, CID):
        super().__init__()
        self.setupUi(self)
        self.CID = CID
        self.Courses = 0
        data = fbh.find_user_by_id(fbh.convert_base(CID, to_base=16))
        self.Avtar, cid, self.Courses, email, self.Nick, password, self.Pproger, self.Teacher = data
        # необходимые преобразования
        if self.Avtar:
            self.image_fromBinary(self.Avtar)
            self.Profile_photo_img.setPixmap(QtGui.QPixmap('Data/Images/avatar.jpg'))
            mini = self.image_toSize('Data/Images/avatar.jpg', 31)
            mini.save('Data/Images/avatar_mini.jpg')
            self.Mini_photo_img.setPixmap(QtGui.QPixmap('Data/Images/avatar_mini.jpg'))
        else:
            self.Profile_photo_img.setPixmap(QtGui.QPixmap('Data/Images/First_avatar.png'))
            mini = self.image_toSize('Data/Images/First_avatar.png', 31)
            mini.save('Data/Images/avatar_mini.jpg')
            self.Mini_photo_img.setPixmap(QtGui.QPixmap('Data/Images/avatar_mini.jpg'))
        self.Profile_CID_txt.setText('CID: #' + str(fbh.convert_base(self.CID, to_base=16)).rjust(6, '0'))
        self.Profile_nickname_txt.setText(self.Nick)
        self.Profile_pproger_txt.setText('P-proger: ' + self.Pproger * 'on' + int(not bool(self.Pproger)) * 'off')
        self.Profile_role_txt.setText('Роль: ' + self.Teacher * 'Учитель' + int(not bool(self.Teacher)) * 'Ученик')
        if self.Pproger:
            self.Profile_proround_img.show()
        self.Mini_CID_txt.setText('CID: #' + str(fbh.convert_base(self.CID, to_base=16)).rjust(6, '0'))
        self.Mini_nick_txt.setText(self.Nick)
        # кнопки
        self.Mini_profile_txt.clicked.connect(self.choose_profile)
        self.Mini_courses_txt.clicked.connect(self.choose_courses)
        self.Mini_pproger_txt.clicked.connect(self.choose_pproger)
        self.Mini_about_txt.clicked.connect(self.choose_about)
        self.Profile_CID_txt.clicked.connect(self.copy)
        self.Profile_choose_btn.clicked.connect(self.choose_avatar)
        self.Courses_first_btn.clicked.connect(self.go_course)

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        try:
            if event.key() == Qt.Key_F10:
                wiki_box(self.Mini_wiki_edit.text())
        except Exception as e:
            error_box('Произошла непредвиденная ошибка')
            print(f'F10: {e}')

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        try:
            if event.MouseButtonDblClick:
                self.Mini_wiki_edit.setEnabled(not self.Mini_wiki_edit.isEnabled())
        except Exception as e:
            error_box('Произошла непредвиденная ошибка')
            print(f'MOUSE: {e}')

    def copy(self):
        try:
            pclip.copy(self.Profile_CID_txt.text()[6:])
        except Exception as e:
            error_box('Произошла непредвиденная ошибка')
            print(f'COPY: {e}')

    def choose_profile(self):
        self.Profile_main_img.show()
        self.Courses_main_img.hide()
        self.Courses_second_img.hide()
        self.Courses_first_img.hide()
        self.Courses_second_btn.hide()
        self.Courses_first_btn.hide()
        self.Pproger_main_img.hide()
        self.About_main_img.hide()
        self.About_txt.hide()

    def choose_courses(self):
        self.Profile_main_img.hide()
        self.Courses_main_img.show()
        self.Courses_second_img.show()
        self.Courses_first_img.show()
        self.Courses_second_btn.show()
        self.Courses_first_btn.show()
        self.Pproger_main_img.hide()
        self.About_main_img.hide()
        self.About_txt.hide()

    def choose_pproger(self):
        self.Profile_main_img.hide()
        self.Courses_main_img.hide()
        self.Courses_second_img.hide()
        self.Courses_first_img.hide()
        self.Courses_second_btn.hide()
        self.Courses_first_btn.hide()
        self.Pproger_main_img.show()
        self.About_main_img.hide()
        self.About_txt.hide()

    def choose_about(self):
        self.Profile_main_img.hide()
        self.Courses_main_img.hide()
        self.Courses_second_img.hide()
        self.Courses_first_img.hide()
        self.Courses_second_btn.hide()
        self.Courses_first_btn.hide()
        self.Pproger_main_img.hide()
        self.About_main_img.show()
        self.About_txt.show()

    def choose_avatar(self):
        avatar = None
        new_avatar = None
        avatar_mini = None
        try:
            avatar_d = QFileDialog.getOpenFileName(self, "Open file", 'C:', 'JPG File (*.jpg);;PNG File (*.png)')
            avatar = Image.open(avatar_d[0])
        except BaseException as e:
            print(f'OpenError: {e}')
        # корректировка изображения
        try:
            avatar.save('Data/Images/avatar.jpg')
            new_avatar = self.image_toSize('Data/Images/avatar.jpg', 133)
            avatar_mini = self.image_toSize('Data/Images/avatar.jpg', 31)
        except Exception as e:
            print(f'SizeError: {e}')
        # сохранение и установка аватарки
        try:
            new_avatar.save('Data/Images/avatar.jpg')
            bin_img = self.image_toBinary('Data/Images/avatar.jpg')
            fbh.update_image(self.CID, bin_img)
            self.Profile_photo_img.setPixmap(QtGui.QPixmap('Data/Images/avatar.jpg'))
            avatar_mini.save('Data/Images/avatar_mini.jpg')
            self.Mini_photo_img.setPixmap(QtGui.QPixmap('Data/Images/avatar_mini.jpg'))
        except Exception as e:
            print(f'BinaryError: {e}')

    def go_course(self):
        try:
            self.course_name = self.sender().objectName()
            self.course = CourseWidget(self.CID, self.course_name, self.Teacher)
            self.course.show()
            self.close()
        except Exception as e:
            print(f'GOCOURSE/288: {e}')

    def image_toBinary(self, img_path):
        with open(img_path, 'rb') as f:
            binary = b64encode(f.read())
        return binary

    def image_fromBinary(self, binary):
        img = BytesIO(b64decode(eval(binary)))
        pil_img = Image.open(img)
        pil_img.save('Data/Images/avatar.jpg')

    def image_toSize(self, img_path, img_size):
        new_img = Image.open(img_path)
        if new_img.size[0] > new_img.size[1]:
            delta = img_size / float(new_img.size[1])
            x = int(float(new_img.size[0]) * delta)
            y = int(float(new_img.size[1]) * delta)
            cropy = ((x - img_size) // 2, 0, (x - img_size) // 2 + img_size, img_size)
            new_img = new_img.resize((x, y)).crop(cropy)
        else:
            delta = img_size / float(new_img.size[0])
            x = int(float(new_img.size[0]) * delta)
            y = int(float(new_img.size[1]) * delta)
            cropy = (0, (y - img_size) // 2, img_size, (y - img_size) // 2 + img_size)
            new_img = new_img.resize((x, y)).crop(cropy)
        return new_img


# класс Окна_Курсов (преподавание)
class CourseWidget(QMainWindow, Cours_Window):
    def __init__(self, CID, course_name, teacher):
        super().__init__()
        self.setupUi(self)
        self.CID = CID
        self.Teacher = teacher
        self.course_name = course_name
        self.progress = fbh.get_user_progress(self.CID, self.course_name)
        self.Name_txt.setText((self.course_name == 'BASE') * 'Основы программирования на Python' + \
                              (self.course_name == 'PRO') * 'Начало разработки на Python')
        if self.Teacher:
            self.teaher_btn.show()
            self.teaher_btn.clicked.connect(self.go_tests)
        # кнопки
        self.Back_btn.clicked.connect(self.go_table)
        # уроки
        folder = Path(f'Data/Texts/{course_name}')
        if not folder.is_dir():
            raise ValueError(f"[{folder}] не существует или не является директорией")
        for i in range(len(list(folder.iterdir())) - 1):
            try:
                exec(f'self.lesson{i}_btn = ClickedLabel()')
                exec(f'self.lesson{i}_btn.setGeometry(QtCore.QRect(0, 0, 980, 130))')
                exec(f'self.lesson{i}_btn.setText("")')
                exec(f'self.lesson{i}_btn.setPixmap(QtGui.QPixmap("Data/Images/PyTutorial_Courses_3_{i}.png"))')
                exec(f'self.lesson{i}_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))')
                exec(f'self.lesson{i}_btn.setObjectName("btn{i}")')
                exec(f'self.lesson{i}_btn.clicked.connect(self.go_lesson)')
                exec(f'if {i} > int({fbh.get_user_progress(self.CID, self.course_name)}):\n'\
                     f'    self.lesson{i}_btn.hide()')
                exec(f'self.layoutScrollMain.addWidget(self.lesson{i}_btn)')
            except ConnectionExcept:
                error_box('Ошибка подключения!')
            except Exception as e:
                print(f'NEWLESSON/320: {e}')
        self.scrollAreaWidget.setLayout(self.layoutScrollMain)
        self.scrollArea.setWidget(self.scrollAreaWidget)

    def go_table(self):
        try:
            self.table = TableWidget(self.CID)
            self.table.show()
            self.close()
        except Exception as e:
            print(f'GOTABLE/330: {e}')

    def go_lesson(self):
        self.count = 1
        self.lesson_num = int(self.sender().objectName()[3:]) + 1
        self.rollNext_btn.clicked.connect(self.rollLesson)
        self.rollBack_btn.clicked.connect(self.rollLesson)
        course = self.course_name
        lesson = f"{self.course_name}_{self.lesson_num}"
        text = f"{lesson}.{self.count}.txt"
        folder_name = f'Data/Texts/{course}/{lesson}/'
        folder = Path(folder_name)
        self.folder_count = 0
        if folder.is_dir():
            self.folder_count = len([1 for file in folder.iterdir()])
        try:
            with open(f'Data/Texts/{course}/{lesson}/{text}', encoding='utf-8') as file:
                self.Lesson_txt.setText(''.join(file.readlines()))
        except Exception as e:
            self.Lesson_img.hide()
            self.scrollAreaLesson.hide()
        self.Lesson_img.show()
        self.scrollAreaLesson.show()

    def rollLesson(self):
        self.test = 0
        self.out = ''
        self.correct = ''
        roll = (self.sender().objectName() == 'rollNext_btn') - (self.sender().objectName() == 'rollBack_btn')
        self.count += roll
        course = self.course_name
        lesson = f"{self.course_name}_{self.lesson_num}"
        text = f"{lesson}.{self.count}.txt"
        self.editProgram.hide()
        self.results.hide()
        try:
            with open(f'Data/Texts/{course}/{lesson}/{text}', encoding='utf-8') as file:
                self.Lesson_txt.setText(''.join(file.readlines()))
                if self.count == self.folder_count:
                    self.editProgram.show()
                    self.results.show()
                    progress = fbh.get_user_progress_one(self.CID, self.course_name, self.lesson_num)
                    if progress == None:
                        self.check_btn.clicked.connect(self.check_program)
                    elif progress == '':
                        self.error_btn.setPixmap(QtGui.QPixmap('Data/Images/PyTutorial_Courses_8_3.png'))
                    elif progress == 'Зачет':
                        self.error_btn.setPixmap(QtGui.QPixmap('Data/Images/PyTutorial_Courses_8_1.png'))
                    else:
                        self.error_btn.setPixmap(QtGui.QPixmap('Data/Images/PyTutorial_Courses_8_2.png'))
                        self.check_btn.clicked.connect(self.check_program)
                    self.error_btn.clicked.connect(self.my_error)
        except ConnectionExcept:
            error_box('Ошибка подключения!')
        except Exception as e:
            self.count = 1
            self.Lesson_img.hide()
            self.scrollAreaLesson.hide()
            print(f'GOTEST/404: {e}')

    def check_program(self):
        res = True
        text = self.editProgram.toPlainText()
        GoodRes = 'Data/Images/PyTutorial_Courses_8_1.png'
        BadRes = 'Data/Images/PyTutorial_Courses_8_2.png'
        TeachRes = 'Data/Images/PyTutorial_Courses_8_3.png'
        try:
            with open(f'Data/Texts/{self.course_name}/{self.course_name}_RESULTS/{self.course_name}_{self.lesson_num}.txt', 'r', encoding='utf-8') as f:
                tasks = eval(f.readline())
                ok = tasks != "For teacher check"
                if ok:
                    for i in tasks.keys():
                        self.out = ''.join(up(text, tasks[i]))
                        self.correct = i
                        if self.out != i:
                            res = False
                            break
                else:
                    self.error_btn.setPixmap(QtGui.QPixmap(TeachRes))
                    fbh.update_progress(self.CID, self.course_name, self.lesson_num, '')
        except ConnectionExcept:
            error_box('Ошибка подключения!')
        except Exception as e:
            print(f'CHECKPROGRAMM/417: {e}')
        try:
            if res and ok:
                self.error_btn.setPixmap(QtGui.QPixmap(GoodRes))
                fbh.update_progress(self.CID, self.course_name, self.lesson_num, 'Зачет')
            else:
                self.error_btn.setPixmap(QtGui.QPixmap(BadRes))
                fbh.update_progress(self.CID, self.course_name, self.lesson_num, f'OUT:\n{self.out}\nCORRECT:\n{self.correct}')
        except ConnectionExcept:
            error_box('Ошибка подключения!')
        except Exception as e:
            print(f'UPDATEDB/474: {e}')

    def my_error(self):
        program_error_box(fbh.get_user_progress_one(self.CID, self.course_name, self.lesson_num))

    def go_tests(self):
        pass


# запуск
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWidget()
    main.show()
    sys.exit(app.exec_())
