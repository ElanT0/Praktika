import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget
from sqlalchemy import text
from engine import session
import sys
from test import Test

class Auth(QMainWindow):
    def __init__(self):
        super().__init__()
        lt = QVBoxLayout()
        login_label = QLabel()
        login_label.setText("Логин")
        pass_label = QLabel()
        pass_label.setText("Пароль")
        self.login_edit = QLineEdit()
        self.pass_edit = QLineEdit()

