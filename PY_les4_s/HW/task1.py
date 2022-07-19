# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math
tmp = float(input("Which accuracy? "))
str = str(tmp)
d = 0
for i in range(len(str) - 2):
    d += 1
print(f"pi with {tmp} accuracy = {round(math.pi, d)}")