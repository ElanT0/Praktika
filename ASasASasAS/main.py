import sys
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QWidget, QMainWindow, QComboBox, QGridLayout, QMessageBox
import random
from main2 import QuizWidget
from engine import session, text, select

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Окно входа")

        self.lbl_1 = QLabel("Имя пользователя:")
        self.tb_1 = QLineEdit()
        self.lbl_2 = QLabel("Пароль:")
        self.tb_2 = QLineEdit()
        self.btn_1 = QPushButton("Войти")
        self.btn_1.clicked.connect(self.login)

        self.captcha_dialog = CaptchaDialog(parent=self)
        self.captcha_dialog.setModal(True)

        self.login_attempts = 0

        layout = QVBoxLayout()
        layout.addWidget(self.lbl_1)
        layout.addWidget(self.tb_1)
        layout.addWidget(self.lbl_2)
        layout.addWidget(self.tb_2)
        layout.addWidget(self.btn_1)

        self.setLayout(layout)

        widget = QWidget()

        with open("styles.css", "r") as css:
            widget.setStyleSheet(css.read())

    def login(self):

        self.sw = QuizWidget()
        sql = text("SELECT * FROM public.student")
        obj = session.execute(sql)
        for row in obj:
            for login in  row:
                self.login = login
            for password in row:
                self.password = password
            if self.tb_1.text() == self.login and self.tb_2.text() == self.password:
                self.sw.show()
                exe.close()
            else:
        
                self.captcha_dialog.start_timer()
                
                if self.captcha_dialog.exec() == QDialog.DialogCode.Accepted:
                    QMessageBox.information(self, "Успех", "Вы вернулись на окно авторизации")
                
                else:
                    QMessageBox.warning(self, "Ошибка", "Неверные данные и капча")
                    self.login_attempts = 0
                    self.generate_captcha()

        
class CaptchaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Капча")
        self.lbl = QLabel("Введите капчу:")
        self.tb = QLineEdit()
        self.btn = QPushButton("Проверить")
        self.btn.clicked.connect(self.verify_captcha)
        self.generate_captcha()

        
        self.timer_lbl = QLabel("Таймер: 10")
        self.timer_counter = 10
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)

        self.lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timer_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        widget = QWidget()

        layout = QVBoxLayout(widget)
        layout.addWidget(self.lbl)
        layout.addWidget(self.tb)
        layout.addWidget(self.timer_lbl)
        layout.addWidget(self.btn)

        self.setLayout(layout)

            

    def verify_captcha(self):
        captcha = self.tb.text()


        if captcha.lower() == self.lbl.text(): 
            self.accept()
        else:
            self.tb.setDisabled(True)  
            self.timer_counter = 11
            self.timer.start()
            QMessageBox.critical(self, "ERROR", "Капча введена не правильно")

    def start_timer(self):
        self.timer_counter = 10
        self.timer.start()

    def update_timer(self):
        self.timer_counter -= 1
        self.timer_lbl.setText(f"Таймер: {self.timer_counter}")

        if self.timer_counter == 0:
            self.timer.stop()
            self.tb.setDisabled(False)
            self.generate_captcha()
        self.captcha_label = QLabel(self)
        self.captcha_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        

    def generate_captcha(self):
        captcha1 = str(random.randint(1000, 9999))
        self.lbl.setText(captcha1)



app = QApplication(sys.argv)
exe = LoginWindow()
exe.show()
app.exec()
