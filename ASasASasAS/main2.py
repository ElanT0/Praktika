import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QPushButton, QLabel

class QuizWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Тест')
        self.layout = QVBoxLayout()

        self.question_label = QLabel('Что такое ПК?')
        self.layout.addWidget(self.question_label)

        self.answer_a = QRadioButton('a) ПК означает "Программное Королевство" и является платформой для разработки и запуска программ на базе PyQt6.')
        self.layout.addWidget(self.answer_a)

        self.answer_b = QRadioButton('b) ПК означает "Питон Королевская 6" и является фреймворком для создания графических интерфейсов на языке программирования Python.')
        self.layout.addWidget(self.answer_b)

        self.answer_c = QRadioButton('c) ПК означает "Персональный Компьютер" и обозначает компьютерные системы, предназначенные для использования одним человеком.')
        self.layout.addWidget(self.answer_c)

        self.submit_button = QPushButton('Ответить')
        self.submit_button.clicked.connect(self.check_answer)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

    def check_answer(self):
        if self.answer_a.isChecked():
            self.show_result('Неправильно. ПК означает "Персональный Компьютер" и обозначает компьютерные системы, предназначенные для использования одним человеком.')
        elif self.answer_b.isChecked():
            self.show_result('Неправильно. ПК означает "Персональный Компьютер" и обозначает компьютерные системы, предназначенные для использования одним человеком.')
        elif self.answer_c.isChecked():
            self.show_result('Правильно! ПК означает "Персональный Компьютер" и обозначает компьютерные системы, предназначенные для использования одним человеком.')
        else:
            self.show_result('Выберите один из вариантов ответа.')
        self.submit_button.setEnabled(True)

    def show_result(self, message):
        self.result_label = QLabel(message)
        self.layout.addWidget(self.result_label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QuizWidget()
    widget.show()
    sys.exit(app.exec())
