# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# wwweeertrtr => 3w3e1r1t1r1t1r
#ABCABCABCDDDFFFFFF => -9ABCABCABC3D6F
from pathlib import Path
path1 = Path(r'task4File.txt')
path2 = Path(r'task4FileOut.txt')


def result(any: str) -> str:
    count = 0
    index = 0
    result = ''
    while(index < len(any) - 1):
        char = any[index]
        count = 0
        for i in range(index, len(any)):
            if(any[i] == char):
                count += 1
            else:
                break
            index += 1
        result =result + f'{count}' + f'{any[index - 1]}'
    return result


count = 0
with open (path1, 'r') as data1:
    for line in data1:
        count += 1
data1 = open(path1, 'r')
data2 = open(path2, 'a')
for i in range(count):
    any = data1.readline()
    data2.write(f'{result(any)}\n')
data1.close()
data2.close()