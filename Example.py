from functools import reduce
from random import getrandbits, randrange, randint
from MyMath import *
from NakasheStern import *
from EncryptCode import *
from DecryptCode import *

if __name__ == '__main__':

    # Генерируем ключи и всю необходимую информацию и получаем класс
    cryptClass = NakasheStern.CreateNakasheSternClass(True)
    # Шифруем сообщение 223 используя только открытые ключи
    encNum = Encrypt.encrypt(223, cryptClass.sigma, cryptClass.g, cryptClass.n)
    # Дешифруем сообщение используя только закрытые ключи и информацию
    decNum = Decrypt.decrypt(encNum, cryptClass.pk, cryptClass.phi, cryptClass.g, cryptClass.n)
    #Печатаем зашифрованный и расшифрованный результат
    print(f'Зашифрованный результат: {encNum}')
    print(f'Дешифрованный результат: {decNum}')