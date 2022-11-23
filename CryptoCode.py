from functools import reduce
from random import getrandbits, randrange, randint
from MyMath import *
from NakasheStern import *
from EncryptCode import *
from DecryptCode import *

# Код для генерации больших простых чисел
# borrowed from here https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb

def is_prime(n, k=128):
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
        r //= 2
    # сделать k тестов
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False

    return True

def generate_prime_candidate(length):
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

def generate_prime_number(length=1024):
    """ Создать простое число
         Аргументы:
             length -- int -- длина генерируемого простого числа в битах
         вернуть простое число
     """
    p = 4
    # продолжаем генерировать, пока не пройден тест на простоту
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p


# Code implementing Chinese Remainder Theorem
# borrowed from https://www.geeksforgeeks.org/using-chinese-remainder-theorem-combine-modular-equations/

# функция, реализующая расширенный алгоритм Евклида
def extended_euclidean(a, b): 
    if a == 0: 
        return (b, 0, 1) 
    else: 
        g, y, x = extended_euclidean(b % a, a) 
        return (g, x - (b // a) * y, y) 

# модульная обратная драйверная функция
def modinv(a, m): 
    g, x, y = extended_euclidean(a, m) 
    return x % m 

# функция, реализующая китайскую теорему об остатках
# список m содержит все модули
# list x содержит остатки уравнений
def crt(m, x): 

        # Мы запускаем этот цикл, пока список
        # остаток имеет длину больше 1
    while True: 
        # temp1 будет содержать новое значение
        # А., который рассчитывается в соответствии с
        # к уравнению m1' * m1 * x0 + m0' * м0 * х1
        temp1 = modinv(m[1],m[0]) * x[0] * m[1] + modinv(m[0],m[1]) * x[1] * m[0] 
        # temp2 содержит значение модуля
        # в новом уравнении, которое будет
        # произведение модулей двух
        # уравнения, которые мы комбинируем
        temp2 = m[0] * m[1] 

        # затем мы удаляем первые два элемента
        # из списка остатков и заменить
        # с остатком, который будет
        # быть temp1 % temp2
        x.remove(x[0]) 
        x.remove(x[0]) 
        x = [temp1 % temp2] + x 

        # затем мы удаляем первые два значения из
        # список модулей, так как они нам больше не нужны
        # их и просто заменить новыми
        # модули, которые мы рассчитали 
        m.remove(m[0]) 
        m.remove(m[0]) 
        m = [temp2] + m 

       # когда в списке останется только один элемент,
       # мы можем выйти, так как он будет содержать только
       # значение нашего последнего остатка
        if len(x) == 1: 
            break

    # возвращает остаток от окончательного уравнения
    return x[0] 


def divide(N, D):
  if D < 0:
    (Q, R) = divide(N, D * -1)
    return (Q * -1, R)
  if N < 0:
    (Q,R) = divide(N * -1, D)
    if R == 0:
        return (Q*-1, 0)
    else:
        return (Q * -1 - 1, D - R)
  # Здесь N >= 0 и D >= 0
  return divide_unsigned(N, D)

def divide_unsigned(N, D):
    Q = 0
    R = N
    while R >= D:
        Q = Q + 1
        R = R - D
    return (Q, R)


class NakacheSternCryptosystem:
    def __init__(self, pk, a, b, g):
        """
        k - кол-во простых чисел p1, ..., pk - списка pk
        pk - список простых чисел p1, ..., pk
        a, b - простые числа. Используются в генерации p и q(см. алгоритм генерации ключа в криптосистеме
            Накаше-Штерна)
        g - основание, которое нужно возводить в степень шифруемого сообщения
        """
        if len(pk) % 2 != 0:
            print("k должно быть чётным")
        self.g = g
        self.pk = pk
        k = len(pk)
        p = 2 * a * reduce(lambda x, y: x*y, pk[:int(k/2)]) + 1
        
        print(reduce(lambda x, y: x*y, pk[int(k/2):]))


        q = 2 * b * reduce(lambda x, y: x*y, pk[int(k/2):]) + 1
        self.sigma = reduce(lambda x, y: x*y, pk)
        #
        print(self.sigma % 2 == 0)
        print(freeSqueareNumber(self.sigma))
        #
        self.n = p * q #21211 #928643
        self.phi = (p - 1) * (q - 1)
        
    def encrypt(self, m):
        x = generate_prime_number(length=len(bin(self.n)) - 2) #19697446673
        # x ^ sigma % n
        x = pow(x, self.sigma, self.n)
        g = pow(self.g, m, self.n)
        return pow(x * g, 1, self.n)


    def decrypt(self, c):
        mk = []
       
        for pi in self.pk:
            ci = pow(c, int(self.phi / pi), self.n)
            for j in range(0, pi):
                if ci == pow(self.g, int(self.phi * j / pi), self.n):
                    mk.append(j)
        return crt(list(self.pk), list(mk))


if __name__ == '__main__':
    crypt = NakacheSternCryptosystem([3, 5, 7, 11, 13, 17], 101, 191, 131)
    tmp = crypt.encrypt(202)
    # print(type(tmp))
    # print(tmp)
    # print(crypt.decrypt(tmp))# 202
    # print(divide(7,2))

    arrayNumbers = generate_array_prime_number(lenght=4, maxInt=20)
    print(arrayNumbers)
    
    #EncClass = Encrypt([3, 5, 7, 11, 13, 17], 101, 191, 131)
    EncClass = None
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
            encMessage: int = Encrypt.encrypt(220, NSC.sigma, NSC.g, NSC.n)
            print(encMessage)
            print(Decrypt.decrypt(encMessage, NSC.pk, NSC.phi, NSC.g, NSC.n))
            print(f"Count Error {countError}")
            print(f"pk = {NSC.pk}")
            print(f"n = {NSC.n}")
            print(f"p = {NSC.p}")
            print(f"q = {NSC.q}")
            print(f"sigma = {NSC.sigma}")
            print(f"g = {NSC.g}")
            break
        except:
            countError+=1

# #generate_array_prime_number(8,70)
#     enc = Encrypt([3, 5, 7, 11, 13, 17], generate_prime_small_number(0, [], 300), generate_prime_small_number(0, [], 300), generate_prime_small_number(0, [], 300))
#     mes = enc.encrypt(123123123)
#     print("ENCRYPT -" + mes)
#     dec = Decrypt(enc.pk, enc.g, enc.n, enc.phi)
#     print("ANSWER - " + str(dec.decrypt(mes)))

    # encInfo = EncClass.encrypt(247)
    # print(encInfo)
    # DecClass = Decrypt([3, 5, 7, 11, 13, 17], 131, EncClass.n, EncClass.phi) #pk, g, n, phi
    # #DecClass = Decrypt([3, 5, 7, 11, 13, 17], 101, 191, 131) #pk, g, n, phi
    # print(DecClass.decrypt(encInfo))