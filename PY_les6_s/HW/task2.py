# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

def fillArrayRandom(size: int, startNumber: int, endNumber: int) -> list:
    array = []
    for i in range(size):
        array.append(random. randrange(startNumber, (endNumber + 1)))
    return array


# def productOfElements(array: list)-> list:
#     product = []
#     tmp = 0
#     if(len(array) % 2 == 0):
#         for i in range(len(array) // 2):
#             tmp = array[i] * array[((len(array) - 1) - i)]
#             product.append(tmp)
#     else:
#         for i in range((len(array) // 2) + 1):
#             tmp = array[i] * array[((len(array) - 1) - i)]
#             product.append(tmp)
#     return product


array = fillArrayRandom(int(input("Which size? ")), int(input("From? ")), int(input("To? ")))
if(len(array) % 2 == 0):
    newArray1 = [array[i] for i in range(len(array)// 2)]
    newArray2 = [array[-i] for i in range(1, len(array)// 2 + 1)]
else:
    newArray1 = [array[i] for i in range(len(array)// 2 + 1)]
    newArray2 = [array[-i] for i in range(1, len(array)// 2 + 2)]
result = list(map((lambda x, y: x * y), newArray1, newArray2))
print(array)
print(f'Result is: {result}')