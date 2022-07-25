# Список чисел. Сделать список с последовательностью. Порядок не менять
example = [1,5,2,3,4,6,1,7,8,1,2,34,5,2]

array = [example[0]]
max = example[0]
for i in range(len(example)):
    if(max < example[i]):
        max = example[i]
        array.append(max)
print(array)