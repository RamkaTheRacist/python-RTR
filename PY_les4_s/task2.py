#Найти Ax^2 + Bx + c = 0:
#1) мат формула
#2)библии питона
#d = b^2 - 4ac
#d ==0 => x = -b/2a
#d > 0 => x1,2 = -b +,- sqrt(d) / 2 * a
from pathlib import Path
path = Path(r'filetask2.txt')
def searchX (discriminant: float) -> float:
    match discriminant:
        case 0:
            x = (-b) / (2*a)
            return(round(x, 2))
        case discriminant if discriminant > 0:
            x1 = round((-b + discriminant ** 0.5) / (2 * a), 2)
            x2 = round((-b - discriminant ** 0.5) / (2 * a), 2)
            return (x1,x2)
        case _:
            return ("There is no solution")

with open (path, 'r') as data:
    a = int(data.readline())
    b = int(data.readline())
    c = int(data.readline())
d = (b ** 2) - (4 * a * c)
any = searchX(d)
with open (path, 'a') as data:
    data.write(f"\nx1 = {any[0]}")
    data.write(f"\nx2 = {any[1]}")

