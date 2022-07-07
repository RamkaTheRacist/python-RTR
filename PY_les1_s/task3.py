# input N. Print -N to N

num = int(input("Which N? "))
# for i in range(-num, num + 1):
#     print(i)
count = -num
while(count < (num + 1)):
   print(count)
   count += 1



# кратно ли число 5 и 19 или 15, но не 30
if((num % 5 == 0) and (num % 10 == 0)):
    print(f"{num} кратно 5 и 10")
elif((num % 15 ==0) and (num % 30 != 0)):
    print(f"{num} кратно 15 но не 30")
else:
    print("zzzzz")