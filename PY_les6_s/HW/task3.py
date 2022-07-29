# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#                                               (1 + 1/n)^n
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# def func(number: int):
#     array = []
#     tmp = 1
#     for i in range(1, (number + 1)):
#         tmp = (1 + 1/i) ** i
#         array.append(tmp)
#     return array

number = int(input("Which number? "))
result = [((1 + 1/i) ** i) for i in range(1,number + 1)]
print(result)

