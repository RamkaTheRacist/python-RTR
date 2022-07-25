# list = []
# for i in range (1, 101):
#     if(i%2 == 0):
#         list.append(i)


# list = [(i, i) for i in range(1, 101) if i % 2 == 0]

# list = [i for i in range(1, 101) if i % 2 == 0]
# print(list)

# def f(x):
#     return x**3

# list = [f(i) for i in range(1, 101) if i % 2 == 0]
# print(list)

#################################### My version:

# def f(x):
#     return x**2
# from pathlib import Path
# path = Path(r'task2File.txt')
# with open(path, 'r') as data:
#     string = data.readline()
#     string = string.split(' ')
# list = [(int(i), f(int(i))) for i in string if int(i) % 2 == 0]
# print(list)

################################## In lection:

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()
# res = select(int, data)
# print(res)
# res = where(lambda x: not x%2, res)
# print(res)
# res = select(lambda x: (x, x**2), res)
# print(res)

# array = [i for i in range(1,20)]
# array = list(map(lambda x:x+10, array))
# print(array)

# data = list(map(int,input().split(' ')))
# print(data)

# data = map(int, '1 2 34 9 8 7 6 5 4'.split())
# for i in data:
#     print(i)

# print('daw')
# for i in data:          #Можно пройтись 1 раз без сохранения
#     print(i)


# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = where(lambda x: not x%2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)



# data = [x for x in range(10)]
# res = list(filter(lambda x: not x % 2, data))
# print(res)

data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = list(filter(lambda x: not x%2, res))
res = list(map(lambda x: (x, x**2), res))
print(res)
