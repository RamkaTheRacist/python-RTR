#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def removeRepetiton(array:list, array2:list) -> list:
    for i in range(len(array2)):
        del array[array[len(array2) - i]]
    return array


def positionOfRepetition(array: list) -> list:
    posArray = []
    k = 0
    for i in range(1, len(array)):
        if(array[k] == array[i]):
            posArray.append(i)
        else:
            k+=1
    return posArray



def division(number: int) -> list:
    tmp = number
    array = [1]
    count = 2
    while(tmp != 1):
        if(tmp % count == 0):
            tmp //= count
            array.append(count)
        else:
            count += 1
    return array



num = int(input("Which number? "))
print(f"Result: {division(num)}")
# arrayDirty = division(num)
# arrayPosition = positionOfRepetition(arrayDirty)
# print("Result: {removeRepetiton(arrayDirty, arrayPosition)}")
