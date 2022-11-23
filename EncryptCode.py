from random import getrandbits, randrange
from functools import reduce
from MyMath import *


class Encrypt:
    def encrypt(m, sigma, g, n):
        x = _generate_prime_number(length=len(bin(n)) - 2)
        x = myPow(x, sigma, n)
        newG = myPow(g, m, n)
        return myPow(x * newG, 1, n)

def _generate_prime_number(length=1024):
    """ Создать простое число
        Аргументы:
            length -- int -- длина генерируемого простого числа в битах
        вернуть простое число
    """
    p = 4
    # продолжаем генерировать, пока не пройден тест на простоту
    while not miller_rabi(p, 128):
        p = _generate_prime_candidate(length)
    return p

def _generate_prime_candidate(length):
    """ Генерировать нечетное целое число случайным образом
        Аргументы:
            length -- int -- длина генерируемого числа в битах
        вернуть целое число
    """
    # генерировать случайные биты
    p = getrandbits(length)
    # применяем маску, чтобы установить MSB и LSB в 1
    p |= (1 << length - 1) | 1

    return p
