"""
Задайте список из нескольких чисел.
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""


def summa(a):
    d = len(lst)
    s = 0
    for i in range(1, d, 2):
        s += lst[i]
    return s


lst = []
lst = list(map(int, input("Введите элементы списка (целые числа) через пробел:\n").split()))
print("Сумма элементов на нечетных позициях равна:", summa(lst))