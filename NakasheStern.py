from random import getrandbits, randrange, randint
from functools import reduce
from MyMath import *
from EncryptCode import *
from DecryptCode import *

class NakasheStern:
    def __init__(self, pk, a, b, g):
        """
        k - кол-во простых чисел p1, ..., pk - списка pk (должен быть чётным)
        pk - список простых чисел p1, ..., pk
        a, b - простые числа. Используются в генерации p и q (так же простые числа)
        g - основание, которое нужно возводить в степень шифруемого сообщения
        sigma - перемножение всех чисел из массива pk
        n - p * q
        phi - (p-1) * (q-1)
        """
        self.a = a
        self.b = b
        self.g = g
        self.pk = pk
        k = len(pk)
        if k % 2 != 0:
            raise ValueError("Количество простых чисел в массиве PK должно быть чётным")

        self.p = 2 * a * reduce(lambda x, y: x*y, pk[:myDivide(k,2)]) + 1
        self.q = 2 * b * reduce(lambda x, y: x*y, pk[myDivide(k,2):]) + 1
        if not is_prime_enumeration(self.p) or not is_prime_enumeration(self.q):
            raise ValueError("P и Q должны быть простыми числами")

        self.sigma = reduce(lambda x, y: x*y, pk)
        if self.sigma % 2 == 0 or not freeSqueareNumber(self.sigma):
            raise ValueError("Sigma должно быть не чётным числом, а также свободным от квадратов")


        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)

    # Генерация и проверка значений (шифруем-расшифруем)
    def CreateNakasheSternClass(debugMode: bool = False):
        countError = 0
        while True:
            while True:
                try:
                    countArray = 10
                    while True:
                        countArray = randint(4,11)
                        if countArray % 2 == 0:
                            break 
                    NSC = NakasheStern(generate_array_prime_number(countArray,70), generate_prime_small_number(0, [], 300), generate_prime_small_number(0, [], 300), generate_prime_small_number(0, [], 300))
                    break
                except:
                    countError+=1
            try:
                encMessage: int = Encrypt.encrypt(99999, NSC.sigma, NSC.g, NSC.n)
                # Для простого отслеживания значений
                if(debugMode):
                    print(encMessage)
                    print(Decrypt.decrypt(encMessage, NSC.pk, NSC.phi, NSC.g, NSC.n))
                    print(f"Count Error {countError}")
                    print(f"pk = {NSC.pk}")
                    print(f"n = {NSC.n}")
                    print(f"p = {NSC.p}")
                    print(f"q = {NSC.q}")
                    print(f"sigma = {NSC.sigma}")
                    print(f"g = {NSC.g}")
                return NSC
            except:
                countError+=1