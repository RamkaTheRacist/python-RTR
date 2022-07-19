#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random

def fillArrayRandom(size: int, startNumber: int, endNumber: int) -> list:
    array = []
    for i in range(size):
        array.append(random. randrange(startNumber, (endNumber + 1)))
    return array

array = fillArrayRandom(int(input("Which size? ")), int(input("From? ")), int(input("To? ")))
print(f"Was: {array}")
bool = True
k = 0
while(bool == True):
    count = array.count(array[k])
    if(count > 1):
        check = array[k]
        for i in range(count):
            array.remove(check)
    elif(count == 1):
        k+=1
    if(k > (len(array) - 1)):
        bool = False
if(len(array) != 0):
    print(f"Is: {array}")
else:
    print("Nothing here")
