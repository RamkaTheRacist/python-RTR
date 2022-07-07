#Дробное число. Первая цифра дробной
num = float(input("Number? "))
num = num * 10
digit = int(num) % 10               #Явная типизация
if(digit != 0):
    print(digit)
else:
    print("Nothing here")