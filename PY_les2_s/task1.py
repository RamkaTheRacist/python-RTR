# # Напишите программу, которая принимает на вход число N и выдает последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81
def function(number: int):
    tmp = 1
    for i in range(number):
        print(tmp, end = ' ')
        tmp = tmp * (-3)


def function2(number: int):
    array = []
    tmp = 1
    for i in range(number):
        array.append(tmp)
        tmp = tmp * (-3)
    return array



num = int(input("Enter number: "))
function(num)
print("\nSecond version:")
print(function2(num))


