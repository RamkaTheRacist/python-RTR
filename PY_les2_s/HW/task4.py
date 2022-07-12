#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводит пользователь через пробел


def createArray(number: int):
    array = []
    if(number > 0):
        for i in range(-number, (number + 1)):
            array.append(i)
    else:
        for i in range(number, (-number + 1)):
            array.append(i)
    return array



def switchFromStrToInt(text: str):
    array = []
    for i in range(len(text)):
        if(text[i] != ' '):
            any = int(text[i])
            array.append(any)
    return array



def productOfNumber(arrayOfNumbers: int, arrayOfPositions: int):
    product = 1
    for i in range(len(arrayOfPositions)):
        product *= arrayOfNumbers[arrayOfPositions[i]]
    return product



number = int(input("Which number? "))
arrayOfNumbers = createArray(number)
position = input("Which positions? ")
arrayOfPositions = switchFromStrToInt(position)
print(f"Product is {productOfNumber(arrayOfNumbers, arrayOfPositions)}")



