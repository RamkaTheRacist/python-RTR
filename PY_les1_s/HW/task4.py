# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
number = int(input("Which? "))
if(number == 1):
    print("X from infinity to 0, except 0; Y from 0 to infinity, except 0;")
elif(number == 2):
    print("X from 0 to infinity, except 0; Y from 0 to infinity, except 0;")
elif(number == 3):
    print("X from infinity to 0, except 0; Y from infinity to 0, except 0;")    
elif(number == 4):
    print("X from 0 to infinity, except 0; Y from infinity to 0, except 0;")
else:
    print("Wtf?")