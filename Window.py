import sys

from MyMath import *
from EncryptCode import *
from DecryptCode import *
from NakasheStern import *

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator, QFont
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QDialog, 
    QHBoxLayout,
    QWidget,
    QFormLayout,
)

from random import randint

class ErrorDialog(QDialog):
    def __init__(self, errorText):
        super().__init__()

        self.setWindowTitle('Error')
        self.dlgLayout = QVBoxLayout()
        message = QLabel(str(errorText))
        self.dlgLayout.addWidget(message)
        self.setLayout(self.dlgLayout)
        self.exec()

class GenerateKey(QWidget):
    def __init__(self):
        super().__init__()
        self.nakashStern = None
        self.encryptMessage = ''
        self.setWindowTitle('Генерация ключей')
        self.mainInfo = QLabel('Генерация данных и формирования открытого ключа', self)
        self.openKeyInfo = QLabel('Открытые ключи:', self)
        self.closeKeyInfo = QLabel('Закрытие ключи:', self)
        self.mainInfo.setFont(QFont('Cocoa', 16, 500))
        self.closeKeyInfo.setFont(QFont('Cocoa', 14, 500))
        self.openKeyInfo.setFont(QFont('Cocoa', 14, 500))
        
        self.g = QLabel('G = ')
        self.a = QLabel('A = ')
        self.b = QLabel('B = ')
        self.pk = QLabel('PK = ')
        self.p = QLabel('P = ')
        self.q = QLabel('Q = ')
        self.n = QLabel('N = ')
        self.sigma = QLabel('Sigma = ')
        self.phi = QLabel('Phi = ')
        self.bGenerate = QPushButton('Генерация ключей', self)
        self.bGenerate.clicked.connect(self.generated_info)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.mainInfo)
        self.mainLayout.addWidget(self.a)
        self.mainLayout.addWidget(self.b)
        self.mainLayout.addWidget(self.pk)
        self.mainLayout.addWidget(self.phi)
        self.mainLayout.addWidget(self.closeKeyInfo)
        self.mainLayout.addWidget(self.p)
        self.mainLayout.addWidget(self.q)
        self.mainLayout.addWidget(self.openKeyInfo)
        self.mainLayout.addWidget(self.n)
        self.mainLayout.addWidget(self.sigma)
        self.mainLayout.addWidget(self.g)
        self.mainLayout.addWidget(self.bGenerate)
        self.setLayout(self.mainLayout)


    def generated_info(self):
        try:
            self.nakashStern = NakasheStern.CreateNakasheSternClass()
            self.g.setText(f'G = {self.nakashStern.g}')
            self.pk.setText(f'PK = {self.nakashStern.pk}')
            self.a.setText(f'A = {self.nakashStern.a}')
            self.b.setText(f'B = {self.nakashStern.b}')
            self.p.setText(f'P = {self.nakashStern.p}')
            self.q.setText(f'Q = {self.nakashStern.q}')
            self.n.setText(f'N = {self.nakashStern.n}')
            self.sigma.setText(f'Sigma = {self.nakashStern.sigma}')
            self.phi.setText(f'Phi = {self.nakashStern.phi}')
        except Exception as e:
            ErrorDialog(e)


class PrimeNumbers(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Простые числа')
        self.info = QLabel('Проверка чисел на простоту')
        self.info.setFont(QFont('Cocoa', 16, 500))
        self.inputNumber = QLineEdit()
        self.inputNumber.textChanged.connect(self.clearAnswers)
        self.onlyInt = QIntValidator()
        self.inputNumber.setValidator(self.onlyInt)
        self.bCheck1 = QPushButton('Перебор делителя', self)
        self.bCheck2 = QPushButton('Миллера—Рабина', self)
        self.bGenerate = QPushButton('Генерация числа', self)
        self.answer1 = QLabel('...')
        self.answer2 = QLabel('...')
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
            self.inputNumber.setText(str(randint(0,9999999999999999999)))
        except Exception as e:
            ErrorDialog(e)

    def clearAnswers(self):
        try:
            self.answer1.setText('...')
            self.answer2.setText('...')
        except Exception as e:
            ErrorDialog(e)

    def miller(self):
        try:
            if self.inputNumber.text() != '':
                if miller_rabi(int(self.inputNumber.text())):
                    self.answer2.setText('Yes')
                else:
                    self.answer2.setText('No')
        except Exception as e:
                ErrorDialog(e)
            
    def enumerated(self):
        try:
            if self.inputNumber.text() != '':
                if is_prime_enumeration(int(self.inputNumber.text())):
                    self.answer1.setText('Yes')
                else:
                    self.answer1.setText('No')
        except Exception as e:
            ErrorDialog(e)
            

class EncryptWindow(QWidget):
    def __init__(self, nakSternWindow):
        super().__init__()
        self.setWindowTitle('Шифрование')
        # Информация из NakasheStern class
        self.ns = nakSternWindow
        self.info = QLabel('Получение данных и шифрование сообщения')
        self.info.setFont(QFont('Cocoa', 16, 500))
        self.openKeyInfo = QLabel('Открытые ключи:')
        self.sigma = QLabel('Sigma = ')
        self.g = QLabel('G = ')
        self.n = QLabel('N = ')
        self.message = QLineEdit()
        self.bGetInfo = QPushButton('Получение данных', self)
        self.bGetInfo.clicked.connect(self.generated_info)
        self.bEncrypt = QPushButton('Шифрование', self)
        self.bEncrypt.clicked.connect(self.ecnryptFunc)
        self.answer = QLabel(f'Шифрованное сообщение:')

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.info)
        self.mainLayout.addWidget(self.openKeyInfo)
        self.mainLayout.addWidget(self.sigma)
        self.mainLayout.addWidget(self.g)
        self.mainLayout.addWidget(self.n)
        self.mainLayout.addWidget(self.message)
        self.lH1 = QHBoxLayout()
        self.lH1.addWidget(self.bGetInfo)
        self.lH1.addWidget(self.bEncrypt)
        self.mainLayout.addLayout(self.lH1)
        self.mainLayout.addWidget(self.answer)
        self.setLayout(self.mainLayout)


    def generated_info(self):
        try:
            self.sigma.setText(f'Sigma = {self.ns.nakashStern.sigma}')
            self.g.setText(f'G = {self.ns.nakashStern.g}')
            self.n.setText(f'N = {self.ns.nakashStern.n}')
        except Exception as e:
            ErrorDialog(e)

    def ecnryptFunc(self):
        try:
            self.generated_info()
            text = self.message.text()
            encInfo = ''
            for char in text:
                encInfo += str(Encrypt.encrypt(ord(char), self.ns.nakashStern.sigma, self.ns.nakashStern.g, self.ns.nakashStern.n)) + ' '
            
            #self.encInfo = str(EncClass.encrypt(int(self.message.text())))
            self.answer.setText(f'Шифрованное сообщение: {encInfo}')
            self.ns.nakashStern.encryptMessage = encInfo
        except Exception as e:
            ErrorDialog(e)

    def generateNumber(self):
        try:
            self.message.setText(str(randint(0,2147483647)))
        except Exception as e:
            ErrorDialog(e)


class DecryptWindow(QWidget):
    def __init__(self, nakSternWindow):
        super().__init__()
        self.ns = nakSternWindow # Получение окна
        self.setWindowTitle('Дешифрование')
        self.info = QLabel('Получение закрытых ключей и шифрование')
        self.info.setFont(QFont('Cocoa', 16, 500))
        self.closeKeyInfo = QLabel('Закрытие ключи:')
        self.g = QLabel('G = ')
        self.pk = QLabel('PK = ')
        self.n = QLabel('N = ')
        self.phi = QLabel('Phi = ')
        self.encInfo = QLabel('Зашифрованные данные: ')
        self.bGetKey = QPushButton('Получение данных', self)
        self.bGetKey.clicked.connect(self.getInfo)
        self.bDecrypt = QPushButton('Дешифрование данных', self)
        self.bDecrypt.clicked.connect(self.decryptFunc)
        self.answer = QLabel(f'Расшифрованное сообщение:')

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.info)
        self.mainLayout.addWidget(self.closeKeyInfo)
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
            self.g.setText('G = ' + str(self.ns.nakashStern.g))
            self.pk.setText('PK = ' + str(self.ns.nakashStern.pk))
            self.n.setText('N = ' + str(self.ns.nakashStern.n))
            self.phi.setText('Phi = ' + str(self.ns.nakashStern.phi))
            self.encInfo.setText('Зашифрованные данные: ' + self.ns.nakashStern.encryptMessage)
        except Exception as e:
            ErrorDialog(e)

    def decryptFunc(self):
        try:      
            encryptArray = self.ns.nakashStern.encryptMessage.split()
            decText = ''
            for encChar in encryptArray:      
                decText += chr(Decrypt.decrypt(int(encChar), self.ns.nakashStern.pk, self.ns.nakashStern.phi, self.ns.nakashStern.g, self.ns.nakashStern.n))
            self.answer.setText('Расшифрованное сообщение: ' + decText)
            
        except Exception as e:
            ErrorDialog(e)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None  # Random
        self.w2 = None # Encrypt
        self.w3 = None # Decrypt
        self.w4 = None # Key
        self.setWindowTitle('Накаше-Штерна')

        mainWindget = QWidget()     
        lineEdit4 = QLabel('Генерация ключей', alignment = Qt.AlignmentFlag.AlignCenter)
        button4 = QPushButton('Открыть')   
        button4.clicked.connect(self.show_new_window4)
        lineEdit1 = QLabel('Проверка числа на простоту', alignment = Qt.AlignmentFlag.AlignCenter)
        button1 = QPushButton('Открыть')
        button1.clicked.connect(self.show_new_window)
        lineEdit2 = QLabel('Шифрование', alignment = Qt.AlignmentFlag.AlignCenter)
        self.button2 = QPushButton('Открыть')
        self.button2.clicked.connect(self.show_new_window2)
        lineEdit3 = QLabel('Дешифрование', alignment = Qt.AlignmentFlag.AlignCenter)
        self.button3 = QPushButton('Открыть')
        self.button3.clicked.connect(self.show_new_window3)
        layout = QFormLayout()
        layout.addRow(lineEdit4, button4)
        layout.addRow(lineEdit1, button1)
        layout.addRow(lineEdit2, self.button2)
        layout.addRow(lineEdit3, self.button3)
        self.button2.setDisabled(True)
        self.button3.setDisabled(True)
        mainWindget.setLayout(layout)
        self.setCentralWidget(mainWindget)

    def show_new_window(self, checked):
        if self.w is None:
            self.w = PrimeNumbers()
        self.w.show()
    def show_new_window2(self, checked):
        if self.w2 is None:
            if(self.w4 is None):
                ErrorDialog('Необходимо сначала сгенерировать ключи')
            else:
                self.w2 = EncryptWindow(self.w4)
                self.w2.show()
                self.button3.setDisabled(False)
    def show_new_window3(self, checked):
        if self.w3 is None:
            if(self.w4 is None or self.w2 is None):
                ErrorDialog('Необходимо сначала сгенерировать ключи')
            else:
                self.w3 = DecryptWindow(self.w4)
                self.w3.show() 
    def show_new_window4(self, checked):
        self.button2.setDisabled(False)
        if self.w4 is None:
            self.w4 = GenerateKey()
        self.w4.show()




app = QApplication(sys.argv)
mw = MainWindow()
mw.show()
app.exec()