#2 числа на вход. Проверка одно число является квад другого?
first_num = int(input("First number? "))
second_num = int(input("Second number? "))
if(first_num * first_num == second_num):
    print("True")
elif(second_num * second_num == first_num):
    print("True")
else:
    print("False")
