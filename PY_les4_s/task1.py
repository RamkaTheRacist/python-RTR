#Строка из набора чисел на вход. На вывод: большее и меньшее число. Сепарация через пробел
from pathlib import Path
path = Path(r'filetask1.txt')

def splitText(text: str) -> list:
    array = text.split(' ')
    return array


def convert(inputArray: list) -> list:
    array = []
    for i in range(len(inputArray)):
        tmp = int(inputArray[i])
        array.append(tmp)
    return array


def searchMinMax(array:list) -> int:
    min = array[0]
    max = array[0]
    for i in range(len(array)):
        if(max < array[i]):
            max = array[i]
        if(min > array[i]):
            min = array[i]
    return (min, max)



# userString = input("Write number: ")

# tmp = searchMinMax(convert(splitText(userString)))
# print(f"Min = {tmp[0]}, Max = {tmp[1]}")
with open (path, 'r') as data:
    inputData = data.read()
tmp = searchMinMax(convert(splitText(inputData)))
print(f"Min = {tmp[0]}, Max = {tmp[1]}")


