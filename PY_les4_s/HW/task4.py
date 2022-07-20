# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
from pathlib import Path
path = Path(r'Task4File.txt')
a =  f'{random. randrange(0, 101)} * x ** 2 + '
b =  f'{random. randrange(0, 101)} * x + '
c =  f'{random. randrange(0, 101)}'
if(int(a[:2]) == 0):
    a = ''
if(int(b[:2]) == 0):
    b = ''
if(len(a) + len(b) + len(c) == 0):
    c = '0' 

with open (path, 'a') as data:
    data.write(f'{a}{b}{c} = 0\n')
