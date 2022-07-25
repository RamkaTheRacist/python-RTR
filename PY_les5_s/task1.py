# Файл с N последовательностью натуральных чисел, sep = ' '. Последовательность A[i] - 1 = A[i - 1]. Найти нехватающее число
# Пример 1 2 3 4 5 7 8 9 -> 6
from pathlib import Path
path = Path(r'task1File.txt')
with open(path, 'r') as data:
    string = data.readline()
array = list(map(int, string.split()))

tmp = -1
for i in range(len(array)):
    if(array[i] - 1 != array[i - 1]):
        tmp = array[i] - 1
print(tmp)

# my_list = [1, 2, 4, 5, 6]

# f = lambda i: (my_list[i] - my_list[i - 1]) != 1
# x = tuple(filter(f, range(1, len(my_list))))
# print(x[0] + 1)