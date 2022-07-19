#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
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

