# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def fillArrayRandom(size: int, startNumber: int, endNumber: int) -> list:
    array = []
    tmp = 0
    anyDigit = 0
    for i in range(size):
        anyDigit = random. randrange(0, 100) / 100
        tmp = random. randrange(startNumber, (endNumber + 1)) + anyDigit
        array.append(tmp)
    return array

def convert(array: list) -> list:
    for i in range(len(array)):
        array[i] = round(array[i] - int(array[i]), 2)
    return array


def diffBetweenMaxAndMin(array:list) -> float:
    max = array[0]
    min = array[0]
    diff = 0
    for i in range(1, len(array)):
        if(max < array[i]):
            max = array[i]
        if(min > array[i]):
            min = array[i]
    diff = round(max - min, 2)
    return diff



array = fillArrayRandom(int(input("Size? ")),int(input("From? ")),int(input("To? ")))
print(array)
convert(array)
print(diffBetweenMaxAndMin(array))