import sys

from MyMath import *
from EncryptCode import *
from DecryptCode import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QDialog, 
    QHBoxLayout,
    QWidget,
    QFormLayout,
    QDialogButtonBox
)

from random import randint

class ErrorDialog(QDialog):
    def __init__(self, errorText):
        super().__init__()

        self.setWindowTitle("Error")
        self.dlgLayout = QVBoxLayout()
        message = QLabel(str(errorText))
        self.dlgLayout.addWidget(message)
        self.setLayout(self.dlgLayout)
        self.exec()


class PrimeNumbers(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Простые числа")
        self.info = QLabel("Проверка чисел на простату")
        self.inputNumber = QLineEdit()
        self.inputNumber.textChanged.connect(self.clearAnswers)
        self.inputNumber.setText="123"
        self.onlyInt = QIntValidator()
        self.inputNumber.setValidator(self.onlyInt)
        self.button1 = QPushButton("Ферма", self)
        self.button2 = QPushButton("Миллера—Рабина", self)
        self.button1.setFixedSize(150,30)
        self.button2.setFixedSize(150,30)
        self.answer1 = QLabel("...")
        self.answer2 = QLabel("...")
        self.button1.clicked.connect(self.ferma)
        self.button2.clicked.connect(self.miller)

        self.layout = QVBoxLayout()
        self.hL1 = QHBoxLayout()
        self.hL2 = QHBoxLayout()
        self.hL3 = QHBoxLayout()
        self.hL4 = QHBoxLayout()
        self.hL1.addWidget(self.info, alignment = Qt.AlignmentFlag.AlignCenter)
        self.hL2.addWidget(self.inputNumber)
        self.hL3.addWidget(self.button1, alignment = Qt.AlignmentFlag.AlignCenter)
        self.hL3.addWidget(self.button2, alignment = Qt.AlignmentFlag.AlignCenter)
        self.hL4.addWidget(self.answer1, alignment = Qt.AlignmentFlag.AlignCenter)
        self.hL4.addWidget(self.answer2, alignment = Qt.AlignmentFlag.AlignCenter)
        self.layout.addLayout(self.hL1)
        self.layout.addLayout(self.hL2)
        self.layout.addLayout(self.hL3)
        self.layout.addLayout(self.hL4)
        self.setLayout(self.layout)
        self.layout.setSpacing(10)
        self.setFixedSize(350,200)

    def clearAnswers(self):
        try:
            self.answer1.setText("...")
            self.answer2.setText("...")
        except Exception as e:
            ErrorDialog(e)

    def miller(self):
        try:
            if self.inputNumber.text() != "":
                if miller_rabi(int(self.inputNumber.text())):
                    self.answer2.setText("Yes")
                else:
                    self.answer2.setText("No")
        except Exception as e:
                ErrorDialog(e)
            
    def ferma(self):
        try:
            if self.inputNumber.text() != "":
                if is_prime_ferma(int(self.inputNumber.text())):
                    self.answer1.setText("Yes")
                else:
                    self.answer1.setText("No")
        except Exception as e:
            ErrorDialog(e)
            

class AnotherWindow2(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Шифрование")
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0,100))
        layout.addWidget(self.label)
        self.setLayout(layout)

class AnotherWindow3(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Дешифрование")
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0,100))
        layout.addWidget(self.label)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None  # No external window yet.
        self.w2 = None
        self.w3 = None
        self.setWindowTitle("Накаше-Штерна")
        self.button = QPushButton("Push for Window")
        #self.button.clicked.connect(self.show_new_window)
        #self.setCentralWidget(self.button)

        mainWindget = QWidget()        
        lineEdit1 = QLabel("Проверка числа на простату", alignment = Qt.AlignmentFlag.AlignCenter)
        button1 = QPushButton("Открыть")
        button1.clicked.connect(self.show_new_window)
        lineEdit2 = QLabel("Шифрование", alignment = Qt.AlignmentFlag.AlignCenter)
        button2 = QPushButton("Открыть")
        button2.clicked.connect(self.show_new_window2)
        lineEdit3 = QLabel("Дешифрование", alignment = Qt.AlignmentFlag.AlignCenter)
        button3 = QPushButton("Открыть")
        button3.clicked.connect(self.show_new_window3)
        layout = QFormLayout()
        layout.addRow(lineEdit1, button1)
        layout.addRow(lineEdit2, button2)
        layout.addRow(lineEdit3, button3)
        mainWindget.setLayout(layout)
        self.setCentralWidget(mainWindget)

    def show_new_window(self, checked):
        if self.w is None:
            self.w = PrimeNumbers()
        self.w.show()
    def show_new_window2(self, checked):
        if self.w2 is None:
            self.w2 = AnotherWindow2()
        self.w2.show()
    def show_new_window3(self, checked):
        if self.w3 is None:
            self.w3 = AnotherWindow3()
        self.w3.show()     


app = QApplication(sys.argv)
mw = MainWindow()
mw.show()
app.exec()