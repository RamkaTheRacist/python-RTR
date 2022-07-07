# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
x1 = float(input("X of first point?" ))
y1 = float(input("Y of first point?" ))
x2 = float(input("X of second point?" ))
y2 = float(input("Y of second point?" ))
tmpx = 0
tmpy = 0
if(x1 < 0 and x2 < 0):
    if (-x1 > -x2):
        tmpx = float((-x1) - (-x2))
    else:
        tmpx = float((-x2) - (-x1))
else:
    if(x1 > x2):
        tmpx = float(x1 - x2)
    else:
        tmpx = float(x2 - x1)
if(y1 < 0 and y2 < 0):
    if(-y1) > (-y2):
        tmpy = float((-y1) - (-y2))
    else:
        tmpy = float((-y2) - (-y1))
else:
    if(y1 > y2):
        tmpy = float(y1 - y2)
    else:
        tmpy = float(y2 - y1)

distance = round((((tmpx ** 2) + (tmpy ** 2)) ** 0.5), 3)
print(f"Distance between first point and second point is {distance}")
# Спасибо, что делал это уже на C# :)