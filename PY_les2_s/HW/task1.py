# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
def convert_number(number: float) -> int:
    countOfSymbols = len(str(number))
    number *= 10**countOfSymbols
    return int(number)


def sum_of_digits(number: int) -> int:
    digit = 0
    sum = 0
    while(number != 0):
        digit = number % 10
        number //= 10
        sum += digit
    return sum


number = float(input("Which number? "))
tmp = abs(convert_number(number))
print(f"Summ of digits in {number} is {sum_of_digits(tmp)}")
