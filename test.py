from PyQt6.QtWidgets import QMainWindow , QVBoxLayout , QLabel , QWidget

class Test(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Угадай модель машины")
        self.setFixedSize(1000, 1000)
        
        layout = QVBoxLayout()
        lbl_4 = QLabel()

        layout.addWidget(lbl_4)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


   