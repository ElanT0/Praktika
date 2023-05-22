from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 300)

        lbl1 = QLabel("1.Какая буква пропущена: Ц…РК")
        self.rb1_1 = QRadioButton(text="И")
        rb1_2 = QRadioButton(text="Ы")
        vbox = QVBoxLayout()
        widget1 = QWidget()
        widget1.setLayout(vbox)
        vbox.addWidget(lbl1)
        vbox.addWidget(self.rb1_1)
        vbox.addWidget(rb1_2)

        lbl2 = QLabel("2.Какая буква пропущена: М…Л…КО")
        self.rb2_1 = QCheckBox(text="О")
        self.rb2_2 = QCheckBox(text="А")
        vbox2 = QVBoxLayout()
        widget2 = QWidget()
        widget2.setLayout(vbox2)
        vbox2.addWidget(lbl2)
        vbox2.addWidget(self.rb2_1)
        vbox2.addWidget(self.rb2_2)

        rb4 = QPushButton("Вывести результат")
        rb4.clicked.connect(self.next)
        rb4.clicked.connect(self.result)
        vbox4 = QVBoxLayout()
        widget4 = QWidget()
        widget4.setLayout(vbox4)
        vbox4.addWidget(rb4)

        lbl5 = QLabel("Результаты теста: ")
        self.r1 = QLabel()
        self.r2 = QLabel()
        self.res = QLabel()
        vbox5 = QVBoxLayout()
        widget5 = QWidget()
        widget5.setLayout(vbox5)
        vbox5.addWidget(lbl5)
        vbox5.addWidget(self.r1)
        vbox5.addWidget(self.r2)
        vbox5.addWidget(self.res)
        btn_save = QPushButton("Сохранить")
        btn_save.clicked.connect(self.save)
        vbox5.addWidget(btn_save)

        pagelayout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(self.stacklayout)
        pagelayout.addLayout(self.button_layout)

        self.btnb = QPushButton("назад")
        self.btn = QPushButton("вперед")
        self.btnb.clicked.connect(self.back)
        self.btn.clicked.connect(self.next)
        self.button_layout.addWidget(self.btnb)
        self.button_layout.addWidget(self.btn)

        self.stacklayout.addWidget(widget1)
        self.stacklayout.addWidget(widget2)
        self.stacklayout.addWidget(widget4)
        self.stacklayout.addWidget(widget5)

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

        with open ("proba/style.css","r") as css:
            widget.setStyleSheet(css.read())

    def next(self):
        self.stacklayout.setCurrentIndex(self.stacklayout.currentIndex()+1)

    def back(self):
        self.stacklayout.setCurrentIndex(self.stacklayout.currentIndex()-1)

    def result(self):

        if self.rb1_1.isChecked():
            self.r1.setText("1.Верно")
        else:
            self.r1.setText("1.Не верно")

        if self.rb2_1.isChecked():
            self.r2.setText("2.Верно")
            if self.rb2_2.isChecked():
                self.r2.setText("2.Не верно")
        
    def save(self):
        txt1 = f"Ваш результат:{self.r1.text()} \n"
        txt2 = f"Ваш результат:{self.r2.text()} \n"

        with open("proba/results.txt", "w", encoding="utf-8") as f:
            f.write(txt1)
            f.write(txt2)
            Test.close(self)