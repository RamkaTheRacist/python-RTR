#1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

array = ['1', 'afes', '21', 'afws', '412', 'fa', 'sfa4', 4]
number = (input("Which number? "))
a = False
for i in array:
    if number in array:
       a = True
if(a):
    print(f"{number} is in {array}")
else:
    print("Nothing here")