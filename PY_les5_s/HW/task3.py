# Создайте программу для игры в ""Крестики-нолики"".
#1)PVP
#2)PVE
#3)PVE hardmode
import os
def printField(array:list, size:int):
    count = 0
    for i in range(len(array)//size):
        for k in range(len(array)//size):
            print(f'\t {array[count]}',end = '')
            count+=1
        print('\n') 


def clearConsole():
    os.system('cls')


def createArray(number:int) -> list:
    array = ['Empty' for i in range(number**2)]
    return array


def changeSymbol(array:list, index:int, symbolID:int) -> list:
    array[index] = symbol(symbolID)
    return array



def symbol(number:int) -> str:
    if(number == 0):
        return 'X'
    else:
        return 'O'


def victoryInRows(array:list, size):
    victory = False
    index = 0
    while(victory == False):
        while(index < len(array)):
            res = array[index:index+size]
            tmp = array[index]
            if(tmp == 'Empty'):
                index += 1
            elif(res.count(tmp) == size):
                victory = True
                break   
            else:
                index += 3
        break
    return victory

def victoryInColumns(array:list, size):
    victory = False
    index = 0
    while(victory == False):
        while(index < len(array)):
            res = array[index::size]
            tmp = array[index]
            if(tmp == 'Empty'):
                index += 1
            elif(res.count(tmp) == size):
                victory = True
                break   
            else:
                index += 1
        break
    return victory

def victoryInDiagonal(array:list, size):
    victory = False
    index = 0
    res = array[index::size + 1]
    tmp = array[index]
    if(tmp != 'Empty'):
        if(res.count(tmp) == size):
            victory = True
    index = size - 1
    res = array[index:len(array) - 1:size - 1]
    tmp = array[index]
    if(tmp != 'Empty'):
        if(res.count(tmp) == size):
            victory = True
    return victory

def checkDraw(array:list):
    if(array.count("Empty") == 0):
        return True
    else:
        return False


def victory(array, size):
    victory = False
    if(victoryInRows(array, size) == True):
        victory = True
        return victory  
    elif(victoryInColumns(array, size) == True):
        victory = True
        return victory 
    elif(victoryInDiagonal(array, size) == True):
        victory = True
        return victory 
    return victory


def win(number:int)-> str:
    if(number == 0):
        print("First player is boss of this gym")
    else:
        print("Second player is boss of this gym")

def checkFromFool(size:int, array:list) -> int:
    check = True
    while(check != False):
        number = input("Select position: ")
        try:
            tmp = int(number)
        except:
            print("Try harder")
            continue
        if(tmp in array):
            print("This position isnt free")
        elif(0 <= tmp < size):
            return tmp
        elif(tmp < 0):
            print("Try harder")
        elif(tmp >= size):
            print("Choose normally ffs")
    return tmp


def sizeOfField() -> int:
    check = True
    while(check != False):
        number = input("Which size of field? ")
        try:
            tmp = int(number)
        except:
            print("Try harder")
            continue
        if(tmp > 0):
            return tmp
        elif(tmp <= 0):
            print("Try harder")
    return tmp


def game(size:int):
    array = createArray(size)
    player = 0
    move = 0
    history = []
    while(move < (size**size)):
        clearConsole()
        printField(array, size)
        if(player == 0):
                print("First player moves")
                playerChoose = checkFromFool(len(array), history)
                changeSymbol(array, playerChoose, player)
                player = 1
                history.append(playerChoose)
        else:
                print("Second player moves")
                playerChoose = checkFromFool(len(array), history)
                changeSymbol(array, playerChoose, player)
                player = 0
                history.append(playerChoose)
        printField(array, size)
        if(victoryInRows(array, size) == True):
                if(player == 0):
                    win(1)
                    break
                else:
                    win(0)
                    break
        elif(victoryInColumns(array, size) == True):
                if(player == 0):
                    win(1)
                    break
                else:
                    win(0)
                    break
        elif(victoryInDiagonal(array, size) == True):
                if(player == 0):
                    win(1)
                    break
                else:
                    win(0)
                    break
        elif(checkDraw(array) == True):
                print("Draw")
                break     

game(sizeOfField())




