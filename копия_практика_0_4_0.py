# -*- coding: utf-8 -*-
"""Копия Практика 0.4.0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10Vj8dQWBmdbSd1uyIo4oCTp98wK6Ho3v

Введите ваше ФИО:
"""

Сбродов Илья Андреевич

"""***Дисклеймер***

В данной практике запрещено использования функций:


*   sum()
*   min()
*   max()
*   average()
*   reversed()
*   sorted()
*   готовые функции или библиотеки

**Задача 1:**



Интернет-магазин предлагает следующие условия скидок:

*   Для заказов больше 1000 единиц, клиент получает скидку 5%. Если клиент использует промокод SUPERDISCOUNT, он получает скидку 10% (вместо 5%).
*  Для заказов более 5000 единиц, клиент получает скидку 15%, а использование промокода SUPERDISCOUNT увеличивает скидку до 20% (вместо 15%).

Этап 1:
Ввод:
```
Введите стоимость единицы товара: 5
Введите количество товара: 1001
Введите промокод: GiVEMEDISCONT
```

Вывод:

```
Ваша скидка: 5%
Итоговая сумма: 4754.75
```
Этап 2:

Оформите ваш код в виде функции
"""

def discount(cost, cnt, promo):
    disc = 0
    if cnt > 1000:
      if promo == "SUPERDISCOUNT":
        disc = 10
      else:
        disc = 5
    if cnt > 5000:
      if promo == "SUPERDISCOUNT":
        disc = 20
      else:
        disc = 15
    return disc


сost_product = int(input("Введите стоимость единицы товара: "))
cnt_product = int(input("Введите количество товара: "))
promo_code = input("Введите промокод: ")
disc = discount(сost_product, cnt_product, promo_code)
discc = (100 - disc) / 100
summ = cnt_product * сost_product * discc
print(f"Ваша скидка: {disc}%\nИтоговая сумма: {summ}")

"""**Задача 2:**

Этап 1:
Напишите программу способную отфильтровать список и вывести только положительные элементы


Ввод:
```
-1 5 1 2 -3
```

Вывод:

```
5 1 2
```

Этап 2:

Оформите ваш код в виде функции
"""

def filter(spisok):
    sort_spisok = []
    for i in spisok:
        if len(i) == 1:
            sort_spisok.append(i)
    return sort_spisok


list1 = (input()).split()
print(" ".join(filter(list1)))

"""**Задача 3:**

Этап 1:
Напишите программу реализующую Алгоритм Евклида


> Алгоритм Евклида – это алгоритм нахождения наибольшего общего делителя (НОД) пары целых чисел.



Ввод:
```
30 18
```

Вывод:

```
6
```

Этап 2:
Оформите ваш код в виде функции

"""

def Evclid(first, second):
    while first != second:
        if first == second:
            break
        if first > second:
            if first % second == 0:
                break
            if first % second > 1:
                first = first - second
        if first < second:
            if second % first == 0:
                break
            if second % first > 1:
                second = second - first
    return second


a, b = int(input()), int(input())
print(Evclid(a, b))

"""**Задача 4:**

Этап 1:
Напишите функцию программу, которая принимает строку и возвращает список слов и количество их упомнинаний в предложении

Этап 2:
Оформите ваш код в виде функции

Ввод:
```
apple banana apple
```

Вывод:

```
apple: 2,
banana: 1
```
"""

def counting(str1):
    spisok = []
    cnt = []
    for word in string:
        if word not in spisok:
            spisok.append(f"{word}")
            cnt.append(str1.count(word))
    return f"{spisok[0]}: {cnt[0]},\n{spisok[1]}: {cnt[1]}"


string = list(input("Введите строку, в которой хотите подсчитать количество слов: ").split())
print(counting(string))

"""**Задача 5:**

Этап 1:
Детектор анаграмм Напишите программу на Python, которая принимает в качестве входных данных две строки и проверяет, являются ли они анаграммами друг друга

Этап 2:
Оформите ваш код в виде функции

Ввод:
```
listen, silent
```

Вывод:

```
True
```
"""

def anagrams(a, b):
    cnt1 = [a.count(i) for i in a]
    cnt2 = [b.count(i) for i in b]
    cnt = 0
    summ = 0
    for i in a:
        i = 1
        summ += int(i)
    for i in a:
        for j in b:
            if i == j:
                cnt += 1
            if cnt == summ:
                return True


word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")
print(anagrams(word1, word2))

"""**Задача 6:**

Шифр ​​Цезаря

Напишите программу на Python, которая реализует шифр Цезаря, простой метод шифрования, который заменяет каждую букву буквой на фиксированное количество позиций вниз по алфавиту. Программа должна запрашивать у пользователя сообщение и значение сдвига, а затем шифровать и расшифровывать сообщение.

Этап 1:

Напишите код для реализации данной задачи

Этап 2:

Оформите код в виде нескольких функций:

* Зашифровывает сообщение
* Расшифровывает сообщение
"""

def Caesar_s_cipher(str1):
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮ"
    result = ""
    for i in str1:
        mesto = alphabet.find(i)
        new_mesto = mesto + 3
        if i in alphabet:
            result += alphabet[new_mesto]
        else:
            result += i


string = input("Введите строку, которую хотите зашифровать шифром Цезаря: ").upper()
print(Caesar_s_cipher(string))

"""**Задача 7**

Задача: «Банковская система»

Создайте программу Python, которая имитирует базовую банковскую систему. Система должна иметь следующие функции:

Требования
*   Система должна позволять клиентам создавать счета и хранить их балансы.
*   Система должна позволять клиентам вносить и снимать деньги со своих счетов.
*   Система должна позволять клиентам проверять свой текущий баланс.
*   Система должна позволять клиентам переводить деньги между счетами.
*   Система должна отслеживать транзакции (депозиты, снятия и переводы) и иметь возможность печатать детали транзакций.


Задачи
1. Реализуйте банковскую систему, используя только базовые конструкции Python, такие как def, lists, if, elif и else, без классов или словарей.
Определите функции для создания счетов, внесения и снятия денег, получения балансов счетов, перевода денег между счетами, а также создания и печати транзакций.
2. Напишите основную функцию, которая демонстрирует использование банковской системы путем создания счетов, внесения и снятия денег и перевода денег между счетами.
3. Бонусное задание
Реализуйте способ хранения и печати истории транзакций для каждого счета.

Ограничения
Не используйте классы или словари.
Используйте только базовые конструкции Python, такие как def, lists, if, elif и else.

"""

def creature_acc(score, currency):
    return currency + score


def transaction_insert(account, score):
    account1 = account[0] + str(int(account[1:]) + int(score))
    return account1


def transaction_take_off(account, score):
    account1 = account[0] + str(int(account[1:]) - int(score))
    return account1



action = " "
while action != "":
    action = input("Введите номер действия, которое хотите выполнить:"
                   "\n1 - Создать счёт;"
                   "\n2 - Внести или снять деньги со счёта;"
                   "\n3 - Проверка баланса;"
                   "\n4 - Перевод между счётами"
                   "\nВаш запрос: ")
    if action == "1":
        score = input("Введите сумму денег, с которой хотите создать счёт: ")
        currency = input("Введите валюту, в которой будут храниться ваши деньги на счёте: ")
        account = creature_acc(score, currency)
    if action == "2":
        operation = input("Введите действие, которое хотите совершить со своим счётом(внести или снять деньги)"
                          "\nНапишите '+', если хотите внести"
                          "\nили '-', если хотите снять деньги: ")
        if operation == "+":
            score = input("Введите сумму денег, которую хотите внести: ")
            account = transaction_insert(account, score)
        if operation == "-":
            score = input("Введите сумму денег, которую хотите снять: ")
            account = transaction_take_off(account, score)
    if action == "3":
        print(account)
    if action == "4":