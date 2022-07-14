# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def fillArrayRandom(size: int, startNumber: int, endNumber: int) -> list:
    array = []
    for i in range(size):
        array.append(random. randrange(startNumber, (endNumber + 1)))
    return array


def summOfElements(array: list) -> list:
    summ = 0
    for i in range(len(array)):
        if(i % 2 != 0):
            summ += array[i]
    return summ


print("Sum = ", summOfElements(fillArrayRandom(int(input("Which size? ")), int(input("From? ")), int(input("To? ")))))
