# 5 чисел на ввод. Найти макс
array = []
for i in range (5):
    any = int(input(f"Number {i + 1}? "))
    array.append(any)
max = array[0]
for i in range (5):
    if(max < array[i]):
        max = array[i]
print("max = ", max)