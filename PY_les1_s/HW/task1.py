# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number = int(input("Which number of day of week? "))
if((number == 6) or (number == 7)):
    print("Weekend")
elif(0 < number < 6):
    print("Not weekend")
else:
    print("Wtf?")