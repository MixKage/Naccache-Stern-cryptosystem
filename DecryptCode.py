from functools import reduce
from MyMath import *

import MyMath
class Decrypt:
    def __init__(self, pk, g, n, phi):
        """
        k - кол-во простых чисел p1, ..., pk - списка pk
        pk - список простых чисел p1, ..., pk
        a, b - простые числа. Используются в генерации p и q(см. алгоритм генерации ключа в криптосистеме
            Накаше-Штерна)
        g - основание, которое нужно возводить в степень шифруемого сообщения
        """
        self.g = g
        self.pk = pk
        self.n = n # Получаем как открытый ключ
        self.phi = phi # Получаем как открытый ключ
   
    def decrypt(self, c):
        mk = []
       
        for pi in self.pk:
            ci = myPow(c, int(MyMath.myDivide(self.phi, pi)), self.n)
            for j in range(0, pi):
                # print(myPow(self.g, myDivide(self.phi * j, pi), self.n))
                if ci == myPow(self.g, myDivide(self.phi * j, pi), self.n):
                    mk.append(j)
        return crt(list(self.pk), list(mk))

# функция, реализующая китайскую теорему об остатках
# список m содержит все модули
# list x содержит остатки уравнений
def crt(m, x): 
    if(len(x)==0):
        print("X = 0")
        return 0
        # Мы запускаем этот цикл, пока список
        # остаток имеет длину больше 1
    while True: 
        # temp1 будет содержать новое значение
        # А., который рассчитывается в соответствии с
        # к уравнению m1' * m1 * x0 + m0' * m0 * х1
        temp1 = modinv(m[1],m[0]) * x[0] * m[1] + modinv(m[0],m[1]) * x[1] * m[0] 
        # temp2 содержит значение модуля
        # в новом уравнении, которое будет
        # произведение модулей двух
        # уравнения, которые мы комбинируем
        temp2 = m[0] * m[1] 

        # затем мы удаляем первые два элемента
        # из списка остатков и заменим
        # с остатком, который будет
        # temp1 % temp2
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

# модульная обратная драйверная функция
def modinv(a, m): 
    g, x, y = extended_euclidean(a, m) 
    return x % m 

# функция, реализующая расширенный алгоритм Евклида
def extended_euclidean(a, b): 
    if a == 0: 
        return (b, 0, 1) 
    else: 
        g, y, x = extended_euclidean(b % a, a) 
        return (g, x - myDivide(b, a) * y, y) 
