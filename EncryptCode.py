from random import getrandbits, randrange
from functools import reduce
from MyMath import *

#Криптосистема Накаша — Штерна

class Encrypt:
    def encrypt(m, sigma, g, n):
        x = _generate_prime_number(length=len(bin(n)) - 2)
        # x ^ sigma % n
        x = myPow(x, sigma, n)
        newG = myPow(g, m, n)
        return myPow(x * newG, 1, n)

# miller-rabi
def _is_prime(n, k=128):
    """ Проверить, является ли число простым
        Аргументы:
            n -- int -- число для проверки
            k -- int -- количество тестов для выполнения
        вернуть True, если n простое число
    """
    # Проверяем, не четно ли n.
    # Но будьте осторожны, 2 — это простое число!
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # найти r и s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r = myDivide(r,2)
    # сделать k тестов
    for _ in range(k):
        a = randrange(2, n - 1)
        x = myPow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = myPow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False

    return True

def _generate_prime_number(length=1024):
    """ Создать простое число
        Аргументы:
            length -- int -- длина генерируемого простого числа в битах
        вернуть простое число
    """
    p = 4
    # продолжаем генерировать, пока не пройден тест на простоту
    while not _is_prime(p, 128):
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
