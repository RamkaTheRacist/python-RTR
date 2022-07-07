# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
coor_x = int(input("Which x? "))
coor_y = int(input("Which y? "))
if((coor_x < 0) and (coor_y > 0)):
    print("1")
elif((coor_x > 0) and (coor_y > 0)):
    print("2")
elif((coor_x < 0) and (coor_y < 0)):
    print("3")
elif((coor_x > 0) and (coor_y < 0)):
    print("4")