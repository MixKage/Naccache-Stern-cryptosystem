from random import getrandbits, randrange
from functools import reduce
from MyMath import *

class NakasheStern:
    def __init__(self, pk, a, b, g):
        """
        k - кол-во простых чисел p1, ..., pk - списка pk
        pk - список простых чисел p1, ..., pk
        a, b - простые числа. Используются в генерации p и q
        g - основание, которое нужно возводить в степень шифруемого сообщения
        """
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
