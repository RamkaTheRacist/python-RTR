# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def function(any1, any2, any3):
    if(any1 == 0):
        if((-(any2 or any3)) == -any2 and -any3):
            print("True")
        else:
            print("False")
    elif(any2 == 0):
        if((-(any1 or any3)) == -any1 and -any3):
            print("True")
        else:
            print("False")
    elif(any3 == 0):
        if((-(any2 or any1)) == -any2 and -any1):
            print("True")
        else:
            print("False")

    else:
        if((-(any1 or any2 or any3)) == -any1 and -any2 and -any3):
            print("True")
        else:
            print("False")



x = float(input("Which X? "))
y = float(input("Which Y? "))
z = float(input("Which Z? "))
function(x, y, z)