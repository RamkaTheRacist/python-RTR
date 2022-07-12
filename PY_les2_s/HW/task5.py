#Реализуйте алгоритм перемешивания списка.
import random

def fillArrayRandom(size: int, startNumber: int, endNumber: int):
    array = []
    for i in range(size):
        array.append(random. randrange(startNumber, endNumber))
    return array


def shuffle(array: int):
    tmp = 0
    tmpIndex = 0
    for i in range(len(array)):
        tmp = array[i]
        tmpIndex = random. randrange(len(array))
        array[i] = array[tmpIndex]
        array[tmpIndex] = tmp
    return array


size = int(input("Which size of array? "))
startNumber = int(input("Fill array from which number? "))
endNumber = int(input("Fill array to which number? "))
array = fillArrayRandom(size, startNumber, endNumber)
print(f"Was: {array}")
array = shuffle(array)
print(f"Is:  {array}")
