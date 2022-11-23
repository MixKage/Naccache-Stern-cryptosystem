import random

# Используем собсвенное возведение в степень по модулю
def myPow(x: int, y: int, N: int):
    return __pow__(x, y, N)

# Используем собсвенное деление (не самый эффективный метод)
def myDivide(N: int, D: int):
    return int(__divide__(N, D))

# Реализация возведения в степень по модулю
# x ** y % N (наш способ гораздо быстрее и менее прожорлив)
def __pow__(x, y, N):
    if (y == 0):
        return 1
    z = __pow__(x, __divide__(y,2), N)
    if (y % 2 == 0):
        return (z * z) % N
    else:
        return (x * z * z) % N

# Генерация массива простых чисел, где простые числа не могут повторяться
def generate_array_prime_number(lenght = 100, maxInt = 214123):
    arrayPrimeNumber = []
    if(lenght % 2 != 0):
        lenght = 10
        raise ValueError('Lenght не может быть не чётным')
    
    for _ in range(lenght):
        if(len(arrayPrimeNumber)==0):
            arrayPrimeNumber.append(generate_prime_small_number(0, [], maxInt))
        else:
            # Каждое следующее простое число будет больше первого сгенерированного
            arrayPrimeNumber.append(generate_prime_small_number(arrayPrimeNumber[0],arrayPrimeNumber,maxInt))

    arrayPrimeNumber.sort()
    return arrayPrimeNumber

# Генерация маленьких простых чисел
def generate_prime_small_number(min: int, arrayPrimeNumber, max = 214123):
    randNum = random.randint(min, max)
    while True:
        if(miller_rabi(randNum) and not (randNum in arrayPrimeNumber)):
            return randNum
        else:
            if randNum % 2 == 0:
                randNum += 1
            else:
                randNum += 2


# Перибор
def is_prime_enumeration(num: int):
    if num % 2 == 0:
        return num == 2
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num

# Ферма
def is_prime_ferma(num: int, test_count=120):
    for i in range(test_count):
        rnd = random.randint(1, num - 1)
        if (__pow__(rnd, (num - 1), num) != 1):
            return False

    return True

# miller-rabi
def miller_rabi(n: int, k=128):
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
        a = random.randrange(2, n - 1)
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

def __divideUnsigned__(N, D):
    Q = 0
    R = N
    while (R >= D):
        Q = Q + 1
        R = R - D
    qr = [Q, R]
    return qr

# Узнать свободное ли число от квадратов
def freeSqueareNumber(num):
    squeareNum = 2
    while True:
        tmpAns = squeareNum ** squeareNum
        if tmpAns > num:
            return True
        if num == tmpAns:
            return False
        squeareNum += 1

# Реализация собственного деления (не эффективный метод для больших чисел)
def __divide__(N, D):
   return N//D
    # qr = [0, 0]
    # if (D < 0):
    #     qr = __divide__(N, D * -1)
    #     qr[0] *= -1
    #     return qr
    # if (N < 0):
    #     qr = __divide__(N * -1, D)
    #     if (qr[1] == 0):
    #         qr[0] *= -1
    #         qr[1] = 0
    #         return qr
    #     else:
    #         qr[0] = qr[0] * -1 - 1
    #         qr[1] = D - qr[1]
    #         return qr
    # # Здесь N >= 0 и D >= 0
    # return __divideUnsigned__(N, D)
