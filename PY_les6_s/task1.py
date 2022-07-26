#[1, 1, 2] -> [2]
import random
def fillArrayRandom(size: int) -> list:
    array = []
    for i in range(size):
        array.append(random. randrange(0, 20))
    return array

array = fillArrayRandom(int(input("Which size? ")))
print(array)
any = [array[i] for i in range(len(array)) if array.count(array[i]) == 1]
print(any)