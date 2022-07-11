#Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
def counter(first_string: str, second_string:str):
    count = 0
    totalCount = 0
    for i in range(len(first_string)):
        if(first_string[i] == second_string[0]):
            count = 0
            for l in range(len(second_string)):
                if(first_string[i + l] == second_string[l]):
                    count+=1
                else:
                    count = 0
            if(count == len(second_string)):
                totalCount += 1
    return totalCount


first_string = input("Enter first string: ")
second_string = input("Enter second string: ")
print(f"Second string is in first string {counter(first_string, second_string)} times")
