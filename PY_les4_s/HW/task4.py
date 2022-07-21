# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
from pathlib import Path
path = Path(r'Task4File.txt')
def fillArrayRandom(size: int) -> list:
    array = []
    for i in range(size):
        array.append(random. randrange(0, 101))
    return array

def writtingString(array: list) -> str:
    stringForResult = ''
    for i in range(len(array)):
        if(i != len(array) - 1):
            if(array[i] != 0):
                stringForResult = stringForResult + f'{array[i]}*x**{len(array) - i} + '
        else:
            if(array[i] != 0):
                stringForResult = stringForResult + f'{array[i]}*x + '
    return stringForResult


k = int(input("Which k? "))
array = fillArrayRandom(k)
result = writtingString(array)
lastNumber = random. randrange(0, 101)
if(lastNumber != 0):
    result = result + f'{lastNumber} = 0'
else:
    result = result[0:-2] + '= 0'

with open (path, 'a') as data:
    data.write(f'{result}\n')
