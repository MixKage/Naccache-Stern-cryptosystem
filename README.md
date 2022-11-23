# Naccache-Stern-cryptosystem
 Шифрование с использованием алгоритма Накаше Штерна
 Возможность шифровать данные используя ассинхронный алгоритм Накаше Штерна
 Функционал программы: 
 * Удобное разбиение всего функционала на независимые окна
 * Генерация простых чисел
 * Шифрование сообщения используя ASCII таблицу
 * Дешифровка используя ASCII таблицу
 * Кроссплатформенность благодаря Python + Qt (pyqt)
 
 ## Example
 ```python
# Генерируем ключи и всю необходимую информацию и получаем класс
cryptClass = NakasheStern.CreateNakasheSternClass(True)
# Шифруем сообщение 223 используя только открытые ключи
encNum = Encrypt.encrypt(223, cryptClass.sigma, cryptClass.g, cryptClass.n)
# Дешифруем сообщение используя только закрытые ключи и информацию
decNum = Decrypt.decrypt(encNum, cryptClass.pk, cryptClass.phi, cryptClass.g, cryptClass.n)
# Печатаем зашифрованный и расшифрованный результат
print(f'Зашифрованный результат: {encNum}') # 315009223425884541435
print(f'Дешифрованный результат: {decNum}') # 223
```
 
 ## Как запустить?
 Запускаем файл Window.py с установленным pyqt
 
 ## Скриншот программы
<img width="1173" alt="ScreenProgram" src="https://user-images.githubusercontent.com/55548743/203661406-6f0d736f-223a-4d61-a2e4-1bfa55e95d85.png">

