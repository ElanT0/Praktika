import sys
import random
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from test import Test
from engine import add_data, text, session

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Вход")

        label_login = QLabel("Логин:")
        self.login_edit = QLineEdit()
        label_password = QLabel("Пароль:")
        self.password_edit = QLineEdit()
        button_auth = QPushButton("Ввод")
        button_reg = QPushButton("Регистрация")
        button_exit = QPushButton("Выход")

        layout = QVBoxLayout()
        layout.addWidget(label_login)
        layout.addWidget(self.login_edit)
        layout.addWidget(label_password)
        layout.addWidget(self.password_edit)
        layout.addWidget(button_auth)
        layout.addWidget(button_reg)
        layout.addWidget(button_exit)

        button_auth.clicked.connect(self.auth)
        button_reg.clicked.connect(self.reg)
        button_exit.clicked.connect(self.exit)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        with open ("test_ss/style.css","r") as css:
            widget.setStyleSheet(css.read())

    def auth(self):
        sql = text("SELECT * FROM public.db")
        obj = session.execute(sql)
        
        for row in obj:
            for login in row:
                self.login = login
            for password in row:
                self.password = password

                if self.login_edit.text() == self.login and self.password_edit.text() == self.password:
                    self.test1 = Test()
                    self.test1.show()
                    self.close()

                else:
                    self.captcha1 = Captcha()
                    self.captcha1.show()

    def reg(self):
        self.registr = Registration()
        self.registr.show()
        self.close()

    def exit(self):
        quit()

class Captcha(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(190,160)
        layout = QVBoxLayout()

        self.captcha = QLabel(str(random.randint(1000,9999)))
        self.captcha_edit = QLineEdit()
        self.label = QLabel("Капча")
        self.captcha_btn = QPushButton("Ввод")
        self.timer_label = QLabel("Таймер: 10")
        self.count = 10
        self.timer_label.setText(str(self.count))
        self.timer = QTimer()

        layout.addWidget(self.label)
        layout.addWidget(self.captcha)
        layout.addWidget(self.captcha_btn)
        layout.addWidget(self.captcha_edit)
        layout.addWidget(self.timer_label)

        self.captcha_btn.clicked.connect(self.captcha_click)
        self.timer.timeout.connect(self.timer_tick)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        with open ("test_ss/style.css","r") as css:
            widget.setStyleSheet(css.read())

    def captcha_click(self):
        if self.captcha_edit.text() == self.captcha.text():
            QMessageBox.information(self, "", "Верно")
            Captcha.close(self)
        else:
            self.captcha_edit.setDisabled(True)
            self.timer.start()
            QMessageBox.critical(self, "", "Ошибка")  

    def timer_tick(self):
        self.timer.start(1000)
        self.count -= 1
        self.timer_label.setText(str(self.count))

        if self.count == 0:
            self.timer.stop()
            self.captcha_edit.setDisabled(False)      

class Registration(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Регистрация")

        self.log1 = QLineEdit()
        self.pas1 = QLineEdit()

        label_log1 = QLabel("Логин:")
        label_pas1 = QLabel("Пароль:")

        button_reg1 = QPushButton("Ввод")

        layout = QVBoxLayout()
        layout.addWidget(label_log1)
        layout.addWidget(self.log1)
        layout.addWidget(label_pas1)
        layout.addWidget(self.pas1)
        layout.addWidget(button_reg1)

        button_reg1.clicked.connect(self.btn_add)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        with open ("test_ss/style.css","r") as css:
            widget.setStyleSheet(css.read())

    def btn_add(self):
        login = self.log1.text()
        password = self.pas1.text()
        add_data(login, password)
        
        self.main = Main()
        self.main.show()
        self.close()


app = QApplication(sys.argv)
exe = Main()
exe.show()
sys.exit(app.exec())