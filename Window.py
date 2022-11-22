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
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Простые числа")
        self.info = QLabel("Проверка чисел на простоту")
        self.inputNumber = QLineEdit()
        self.inputNumber.textChanged.connect(self.clearAnswers)
        self.onlyInt = QIntValidator()
        self.inputNumber.setValidator(self.onlyInt)
        self.bCheck1 = QPushButton("Перебор делителя", self)
        self.bCheck2 = QPushButton("Миллера—Рабина", self)
        self.bGenerate = QPushButton("Генерация числа", self)
        self.answer1 = QLabel("...")
        self.answer2 = QLabel("...")
        self.bCheck1.clicked.connect(self.enumerated)
        self.bCheck2.clicked.connect(self.miller)
        self.bGenerate.clicked.connect(self.generateNumber)

        self.layout = QVBoxLayout()
        self.hL1 = QHBoxLayout()
        self.hL2 = QHBoxLayout()
        self.hL3 = QHBoxLayout()
        self.hL4 = QHBoxLayout()
        self.hL1.addWidget(self.info, alignment = Qt.AlignmentFlag.AlignCenter)
        self.hL2.addWidget(self.inputNumber)
        self.hL2.addWidget(self.bGenerate)
        self.hL3.addWidget(self.bCheck1, alignment = Qt.AlignmentFlag.AlignCenter)
        self.hL3.addWidget(self.bCheck2, alignment = Qt.AlignmentFlag.AlignCenter)
        self.hL4.addWidget(self.answer1, alignment = Qt.AlignmentFlag.AlignCenter)
        self.hL4.addWidget(self.answer2, alignment = Qt.AlignmentFlag.AlignCenter)
        self.layout.addLayout(self.hL1)
        self.layout.addLayout(self.hL2)
        self.layout.addLayout(self.hL3)
        self.layout.addLayout(self.hL4)
        self.setLayout(self.layout)
        self.layout.setSpacing(10)
        self.setFixedSize(350,200)

    def generateNumber(self):
        try:
            self.inputNumber.setText(str(randint(0,2147483647)))
        except Exception as e:
            ErrorDialog(e)

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
            
    def enumerated(self):
        try:
            if self.inputNumber.text() != "":
                if is_prime_enumeration(int(self.inputNumber.text())):
                    self.answer1.setText("Yes")
                else:
                    self.answer1.setText("No")
        except Exception as e:
            ErrorDialog(e)
            

class EncryptWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Шифрование")
        self.dec = None
        self.encInfo = ""
        self.info = QLabel("Генерация данных и формирования открытого ключа")
        self.g = QLabel("G = ")
        self.pk = QLabel("PK = ")
        self.p = QLabel("P = ")
        self.q = QLabel("Q = ")
        self.n = QLabel("N = ")
        self.sigma = QLabel("Sigma = ")
        self.phi = QLabel("Phi = ")
        self.message = QLineEdit()
        self.onlyInt = QIntValidator()
        self.message.setValidator(self.onlyInt)
        self.bGenerate = QPushButton("Генерация данных", self)
        self.bGenerate.clicked.connect(self.generated_info)
        self.bEncrypt = QPushButton("Шифрование", self)
        self.bEncrypt.clicked.connect(self.ecnryptFunc)
        self.bGenerateNumber = QPushButton("Генерация числа", self)
        self.bGenerateNumber.clicked.connect(self.generateNumber)
        self.answer = QLabel(f"Шифрованный результат: {self.encInfo}")

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.info)
        self.mainLayout.addWidget(self.g)
        self.mainLayout.addWidget(self.pk)
        self.mainLayout.addWidget(self.p)
        self.mainLayout.addWidget(self.q)
        self.mainLayout.addWidget(self.n)
        self.mainLayout.addWidget(self.sigma)
        self.mainLayout.addWidget(self.phi)
        self.lH1 = QHBoxLayout()
        self.lH2 = QHBoxLayout()
        self.lH1.addWidget(self.message)
        self.lH1.addWidget(self.bGenerateNumber)
        self.lH2.addWidget(self.bGenerate)
        self.lH2.addWidget(self.bEncrypt)
        self.mainLayout.addLayout(self.lH1)
        self.mainLayout.addLayout(self.lH2)
        self.mainLayout.addWidget(self.answer)
        self.setLayout(self.mainLayout)


    def generated_info(self):
        try:
            countArray = 10
            while True:
                countArray = randint(4,12)
                if countArray % 2 == 0:
                    break
            self.dec = Encrypt(generate_array_prime_number(countArray,70), generate_prime_small_number(0, [], 300), generate_prime_small_number(0, [], 300), generate_prime_small_number(0, [], 300))
            self.g.setText(f"G = {self.dec.g}")
            self.pk.setText(f"PK = {self.dec.pk}")
            self.p.setText(f"P = {self.dec.p}")
            self.q.setText(f"Q = {self.dec.q}")
            self.n.setText(f"N = {self.dec.n}")
            self.sigma.setText(f"Sigma = {self.dec.sigma}")
            self.phi.setText(f"Phi = {self.dec.phi}")
        except Exception as e:
            ErrorDialog(e)
    
    def ecnryptFunc(self):
        try:
            tmp = str(self.phi.text())
            if(str(self.phi.text())=="Phi = "):
                self.answer.setText("Шифрованный результат: не хватает данных")
            else:
                EncClass = Encrypt([3, 5, 7, 11, 13, 17], 101, 191, 131)
                self.encInfo = str(EncClass.encrypt(int(self.message.text())))
                self.answer.setText(f"Шифрованный результат: {self.encInfo}")
        except Exception as e:
            ErrorDialog(e)

    def generateNumber(self):
        try:
            self.message.setText(str(randint(0,2147483647)))
        except Exception as e:
            ErrorDialog(e)


class DecryptWindow(QWidget):
    def __init__(self, windowEncrypt: EncryptWindow):
        super().__init__()
        self.windowEncrypt = windowEncrypt # Получение окна
        self.setWindowTitle("Дешифрование")
        self.decInfo = ""
        self.info = QLabel("Получение открытых ключей и дешифрование")
        self.g = QLabel("G = ")
        self.pk = QLabel("PK = ")
        self.n = QLabel("N = ")
        self.phi = QLabel("Phi = ")
        self.encInfo = QLabel("Зашифрованные данные: ")
        self.bGetKey = QPushButton("Получение данных", self)
        self.bGetKey.clicked.connect(self.getInfo)
        self.bDecrypt = QPushButton("Дешифрование данных", self)
        self.bDecrypt.clicked.connect(self.decryptFunc)
        self.answer = QLabel(f"Расшифрованный результат: {self.decInfo}")

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.info)
        self.mainLayout.addWidget(self.g)
        self.mainLayout.addWidget(self.pk)
        self.mainLayout.addWidget(self.n)
        self.mainLayout.addWidget(self.phi)
        self.mainLayout.addWidget(self.encInfo)
        self.lH1 = QHBoxLayout()
        self.lH1.addWidget(self.bGetKey)
        self.lH1.addWidget(self.bDecrypt)
        self.mainLayout.addLayout(self.lH1)
        self.mainLayout.addWidget(self.answer)
        self.setLayout(self.mainLayout)

    def getInfo(self):
        try:
            self.g.setText(self.windowEncrypt.g.text())
            self.pk.setText(self.windowEncrypt.pk.text())
            self.n.setText(self.windowEncrypt.n.text())
            self.phi.setText(self.windowEncrypt.phi.text())
            self.encInfo.setText("Зашифрованные данные: " + self.windowEncrypt.encInfo)
        except Exception as e:
            ErrorDialog(e)

    def decryptFunc(self):
        try:            
            dec = Decrypt([3, 5, 7, 11, 13, 17], self.windowEncrypt.dec.g, self.windowEncrypt.dec.n, self.windowEncrypt.dec.phi)
            print(int(self.windowEncrypt.encInfo))
            self.answer.setText(str(dec.decrypt(int(self.windowEncrypt.encInfo))))
        except Exception as e:
            ErrorDialog(e)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None  # No external window yet.
        self.w2 = None
        self.w3 = None
        self.setWindowTitle("Накаше-Штерна")

        mainWindget = QWidget()        
        lineEdit1 = QLabel("Проверка числа на простоту", alignment = Qt.AlignmentFlag.AlignCenter)
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
            self.w2 = EncryptWindow()
        self.w2.show()
    def show_new_window3(self, checked):
        if self.w3 is None:
            if(self.w2 is None):
                ErrorDialog("Необходимо сначала запустить шифрование")
            else:
                self.w3 = DecryptWindow(self.w2)
                self.w3.show()     



app = QApplication(sys.argv)
mw = MainWindow()
mw.show()
app.exec()