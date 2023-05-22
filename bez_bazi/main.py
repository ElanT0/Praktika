import sys
import random
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from test import Test

class Auth(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Вход")

        label_login = QLabel("Логин: ")
        self.login_edit = QLineEdit()
        label_password = QLabel("Пароль:")
        self.password_edit = QLineEdit()
        button_auth = QPushButton("Ввод")
        button_exit = QPushButton("Выход")
        
        layout = QVBoxLayout()
        layout.addWidget(label_login)
        layout.addWidget(self.login_edit)
        layout.addWidget(label_password)
        layout.addWidget(self.password_edit)
        layout.addWidget(button_auth)
        layout.addWidget(button_exit)

        button_auth.clicked.connect(self.auth)
        button_exit.clicked.connect(self.exit)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        with open ("proba/style.css","r") as css:
            widget.setStyleSheet(css.read())

    def exit(self):
        quit()

    def auth(self):
        login = self.login_edit.text()
        password = self.password_edit.text()
        if login == "1" and password == "1":
            self.test = Test()
            self.test.show()
            exe.close()
        else:
            self.captcha = Captcha()
            self.captcha.show()

class Captcha(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(200,150)

        self.captcha = QLabel(str(random.randint(1000,9999)))
        self.captcha_edit = QLineEdit()
        self.label = QLabel("Капча")
        self.captcha_btn = QPushButton("Ввод")
        self.timer_label = QLabel("Таймер: 10")
        self.count = 10
        self.timer_label.setText(str(self.count))
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timer_tick)
        self.captcha_btn.clicked.connect(self.captcha_click)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.captcha)
        layout.addWidget(self.captcha_btn)
        layout.addWidget(self.captcha_edit)
        layout.addWidget(self.timer_label)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        with open ("proba/style.css","r") as css:
            widget.setStyleSheet(css.read())

    def captcha_click(self):
        if self.captcha_edit.text() == self.captcha.text():
            QMessageBox.information(self, "", "Верно")
            Captcha.close(self)
        else:
            self.count = 10
            self.timer_tick()
            self.captcha_edit.setDisabled(True)
            self.timer.start()
            QMessageBox.critical(self, "", "Неверно")

    def timer_tick(self):
        self.count -= 1
        self.timer_label.setText(str(self.count))
        if self.count == 0:
            self.timer.stop()
            self.captcha_edit.setDisabled(False)

app = QApplication(sys.argv)
exe = Auth()
exe.show()
app.exec()