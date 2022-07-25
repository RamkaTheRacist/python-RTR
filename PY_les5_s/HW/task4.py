# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# wwweeertrtr => 3w3e1r1t1r1t1r
from pathlib import Path
path1 = Path(r'task4File.txt')
path2 = Path(r'task4FileOut.txt')


def compression(any: str) -> str:
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
        result += f'{count}' + f'{any[index - 1]}'
    return result

def changeStrToArrayWithInt(text:str) -> list:
    digit = 0
    array = []
    for i in range(len(text)):
        try:
            digit = int(text[i])
            array.append(digit)
        except:
            array.append(text[i])
    return array

def writeResultFromArrayToStr(array:list) -> str:
    ind = 0
    string = ''
    while(ind < len(array)):
        if(type(array[ind]) == int) & (type(array[ind + 1]) == str):
            string += f'{array[ind + 1]}' * array[ind]
            ind += 2
        elif(type(array[ind]) == int) & (type(array[ind + 1]) == int):
            tmp = array[ind] * 10 + (array[ind + 1])
            string += f'{array[ind + 2]}' * tmp
            ind += 3
    return string


count = 0
with open (path1, 'r') as inputData:
    for line in inputData:
        count += 1
inputData = open(path1, 'r')
compressedData = open(path2, 'a')
for i in range(count):
    any = inputData.readline()
    compressedData.write(f'{compression(any)}\n')
inputData.close()
compressedData.close()
example1 = '9W3B24W1B14W'
example2 = '1A1B1C1A1B1C1A1B1C3D6F'
print("Compressed:", example1)
print("Uncompressed:", writeResultFromArrayToStr(changeStrToArrayWithInt(example1)))
print("Compressed:", example2)
print("Uncompressed:", writeResultFromArrayToStr(changeStrToArrayWithInt(example2)))

