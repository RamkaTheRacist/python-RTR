# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
def fiboFromNullToNumber(number: int) -> list:
    array = [0]
    f0 = 0
    f1 = 1
    f = 1
    i = 0
    while(i < number):
        array.append(f)
        f = f1 + f0
        f0 = f1
        f1 = f
        i+=1 
    return array


def fiboFromNumberToNull(number: int) -> list:
    array = []
    f0 = 0
    f1 = 1
    f = 1
    i = 0
    while(i > -number):
        array.append(f)
        f = f0 - f1
        f0 = f1
        f1 = f
        i-=1 
    return array


def reverseArray(array: list) -> list:
    tmp = 0
    for i in range(len(array) // 2):
        tmp = array[i]
        array[i] = array[len(array) - 1 - i]
        array[len(array) - 1 - i] = tmp
    return array


number = int(input("Which number? "))
print(reverseArray(fiboFromNumberToNull(number)) + fiboFromNullToNumber(number))

