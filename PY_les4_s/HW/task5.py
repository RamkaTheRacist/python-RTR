#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
from pathlib import Path
path1 = Path(r'Task5File1.txt')
path2 = Path(r'Task5File2.txt')
path3 = Path(r'Task5File3.txt')


def countPlusResult(firstString: str, secondString: str) -> str:
    firstArray = firstString[:-4].split(' + ')
    secondArray = secondString[:-4].split(' + ')
    strtmp = ''
    sum = 0
    string = ''
    countFirst = 0
    countSecond = 0
    check = True
    while(check != False):
        tmp1= firstArray[countFirst].split('*')
        tmp2= secondArray[countSecond].split('*')
        if(len(tmp1) == 1) and (len(tmp2) == 1):
            check = False
        else:
            if(len(tmp1) == len(tmp2)):
                if(tmp1[len(tmp1) - 1] != tmp2[len(tmp2) - 1]):
                    if(tmp1[len(tmp1) - 1] > tmp2[len(tmp2) - 1]):
                        strtmp = strtmp + f'{firstArray[countFirst]} '
                        countFirst +=1
                    else:
                        strtmp = strtmp + f'{secondArray[countSecond]} '
                        countSecond +=1
                else:
                    string = ''
                    sum = int(tmp1[0]) + int(tmp2[0])
                    tmp = f'{firstArray[countFirst]}'
                    tmp = tmp.split('*',1)
                    tmp[0] = sum
                    for i in range(len(tmp)):
                        string += f'{tmp[i]}*'
                    string = string[:-1]
                    strtmp += f'{string} '
                    countFirst +=1
                    countSecond +=1
            else:
                if(len(tmp1) > len(tmp2)):
                    strtmp = strtmp + f'{firstArray[countFirst]} '
                    countFirst +=1
                else:
                    strtmp = strtmp + f'{secondArray[countSecond]} '
                    countSecond +=1
    sum = int(firstArray[len(firstArray) - 1]) + int(secondArray[len(secondArray) - 1])
    strtmp += f'{sum}'
    result = strtmp.replace(' ', ' + ')
    result += ' = 0'
    return result


count = 0
with open (path1, 'r') as data1:
    for line in data1:
        count += 1
data1 = open(path1, 'r')
data2 = open(path2, 'r')
data3 = open(path3, 'a')
for i in range(count):
    firstString = data1.readline()
    secondString = data2.readline()
    # print("First:")
    # print(firstString)
    # print("Second:")
    # print(secondString)
    # print("Result")
    # print(countPlusResult(firstString, secondString))
    data3.write(f'{countPlusResult(firstString, secondString)}\n')
data1.close()
data2.close()
data3.close()

