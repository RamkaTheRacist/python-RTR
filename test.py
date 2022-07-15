# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# def function(number):
#     match number:
#         case 6 | 7:
#            return print(f"{number} is weekend")
#         case number if(0 < number < 6):
#            return print(f"{number} is not weekend")
#         case _:
#             return print("????")
# function(int(input("Which day? ")))





# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# def function(number):
#    match number:
#       case number if number % 1 != 0:              # Определение есть ли что-нить после запятой
#          return intSum(convertFloatToInt(number))
#       case _:
#          return intSum(number)



# def convertFloatToInt(number):
#    while(number % 1 != 0):
#       number *= 10
#    return number



# def intSum(number):
#    digit = 0
#    summ = 0
#    while(number != 0):
#       digit = number % 10
#       summ += digit
#       number //=10
#    return int(summ)

# print(function(float(input("which number? "))))


#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводит пользователь через пробел

# def createArray(number: int):
#     array = []
#     if(number > 0):
#         for i in range(-number, (number + 1)):
#             array.append(i)
#     else:
#         for i in range(number, (-number + 1)):
#             array.append(i)
#     return array


# def positions(text: str):
#    args = text.split(' ')
#    array = []
#    for i in range(len(args)):
#       array.append(int(args[i]))
#    return array


# def func(number1, number2):
#    product = 1
#    for i in range(len(number2)):
#       product *= number1[number2[i]]
#    return product


# print(func(createArray(int(input("Which number? "))), positions(input("Positions? "))))


a = {1,2,3,5,8}
b = {2,5,8,13,21}
print(b.intersection(a))
