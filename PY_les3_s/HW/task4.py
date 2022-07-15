# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
def binaryConvert(number: int) -> int:
    result = 0
    tmp = 0
    count = 0
    while(number > 0):
        tmp = number % 2
        number //= 2
        result = result + tmp * 10 ** count
        count += 1
    return result



number = int(input("Which number? "))
print(binaryConvert(number))
