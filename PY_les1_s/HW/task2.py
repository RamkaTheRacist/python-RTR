# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def function(any1, any2, any3):
    if(not (any1 or any2 or any3) == (not any1 and not any2 and not any3)):
        print("True")
    else:
        print("False")



x = float(input("Which X? "))
y = float(input("Which Y? "))
z = float(input("Which Z? "))
function(x, y, z)