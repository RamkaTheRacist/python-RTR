#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random
def removeRepetiton(array:list, array2:list) -> list:
    for i in range(len(array2)):
        del array[array2[len(array2) - 1 - i]]
    return array


def positionOfRepetition(array: list) -> list:
    posArray = []   
    for i in range(len(array)):
        for k in range(i + 1, len(array)):
            if(array[k] == array[i]):
                posArray.append(k)
                break    
    return posArray


def sortOfArray(array: list) -> list:
    index = 0
    while(index < len(array)):
        max = -1
        tmpPos = len(array) - 1 - index
        for i in range(len(array) - index):
            if(max < array[i]):
                max = array[i]
                tmpPos = i
        if(tmpPos != len(array) - index):
            tmp = array[len(array) - 1 - index]
            array[len(array) - 1 - index] = array[tmpPos]
            array[tmpPos] = tmp
        index += 1
    return array


def fillArrayRandom(size: int, startNumber: int, endNumber: int) -> list:
    array = []
    for i in range(size):
        array.append(random. randrange(startNumber, (endNumber + 1)))
    return array

array = fillArrayRandom(int(input("Which size? ")), int(input("From? ")), int(input("To? ")))
print(array)
posArray = positionOfRepetition(array)
sortedArray = sortOfArray(posArray)
print("Now:")
print(removeRepetiton(array, sortedArray))