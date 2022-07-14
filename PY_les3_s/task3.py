#3.Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
import time
def current_milli_time():
    return round(time.time())

number = int(input("Size? "))
tmp = 1
array = []
for i in range ((number + 1) // 3):
    array.append(tmp * (current_milli_time() // 10000))
    array.append((tmp * (current_milli_time() // 10000)) // 3)
    array.append((tmp * (current_milli_time() // 10000)) // 100)
    tmp += 2
print(array)