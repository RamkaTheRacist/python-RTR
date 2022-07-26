# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#1)PVP
#2)PVE
#3)PVE hardmode
import random
import os

def clearConsole():
    os.system('cls')


def choose() -> int:
    choosing = random. randrange(0, 10)
    if(choosing % 2 == 0):
        return 0
    else:
        return 1


def takeCandy() -> int:
    check = True
    while(check != False):
        number = input("How much candies gonna take? ")
        try:
            tmp = int(number)
        except:
            print("Try harder")
            continue
        if(0 < tmp < 29):
            return tmp
        elif(0 >= tmp):
            print("How u gonna take 0 or less than 0?")
        elif(tmp > 28):
            print("Dont be greedy")
    return tmp

def gamePVP(number:int):
    choose = number
    history = ''
    size = 2021
    count = 0
    minus = 0
    while(size > 1):
        clearConsole()
        if(minus == 0):
            print(f'Left {size} candies')
        else:
            if(choose == 0):
                print(f"Second player took {minus}")
                print(f'Left {size} candies')
            else:
                print(f"First player took {minus}")
                print(f'Left {size} candies')
        if(choose == 0):
            print("First player is choosing:")
            minus = takeCandy()
            size -= minus
            choose = 1
            count +=1
            history += f'Move {count} : First player: {minus} | '
        else:
            print("Second player is choosing:")
            minus = takeCandy()
            size -= minus
            choose = 0
            count +=1
            history += f'Move {count} : Second player: {minus} | '
        if(size == 1):
            if(choose == 0):
                
                win(1)
            else:
                win(0)
        else:
            if(choose == 0):
                win(0)
            else:
                win(1)
    print("\nWant to look at history of moves?")
    text = input()
    if(text == 'Yes' or text == 'Yea' or text == 'yes' or text == 'yea' or text == 'da' or text == 'Da' or text == 'ye' or text == 'Ye'):
        print(history)
    else:
        print("bb")


def gamePVE(number:int, botIQ: int):
    choose = number
    history = ''
    size = 2021
    count = 0
    minus = 0
    while(size > 1):
        clearConsole()
        if(minus == 0):
            print(f'Left {size} candies')
        else:
            if(choose == 0):
                print(f"Second player took {minus}")
                print(f'Left {size} candies')
            else:
                print(f"First player took {minus}")
                print(f'Left {size} candies')
        if(choose == 0):
            print("First player is choosing:")
            minus = takeCandy()
            size -= minus
            choose = 1
            count +=1
            history += f'Move {count} : First player: {minus} | '
        else:
            print("Second player is choosing:")
            minus = botMove(size, botIQ)
            size -= minus
            choose = 0
            count +=1
            history += f'Move {count} : Second player: {minus} | '
    if(size == 1):
        if(choose == 0):
            win(1)
        else:
            win(0)
    else:
        if(choose == 0):
            win(0)
        else:
            win(1)
    print("\nWant to look at history of moves?")
    text = input()
    if(text == 'Yes' or text == 'Yea' or text == 'yes' or text == 'yea' or text == 'da' or text == 'Da' or text == 'ye' or text == 'Ye'):
        print(history)
    else:
        print("bb")



def win(number: int) -> str:
    if(number == 0):
        clearConsole()
        print("Second player took last candies")
        print("Second player wins")
    else:
        clearConsole()
        print("First player took last candies")
        print("First player wins")



def modeChoose() -> int:
    clearConsole()
    check = True
    while(check != False):
        number = input("Game types: 1)PVP, 2)PVE-easy, 3)PVP-hard ")
        try:
            tmp = int(number)
        except:
            print("Try harder")
            continue
        if(0 < tmp < 4):
            return tmp
        else:
            print("Try harder")
    return tmp


def typeOfGame(number: int):
    clearConsole()
    if(number == 1):
        print("PVP mode")
        input("Press any key")
        gamePVP(choose())
    elif(number == 2):
        print("PVE Easymode")
        input("Press any key")
        gamePVE(choose(), number)
    else:
        print("PVE Hardmode")
        input("Press any key")
        gamePVE(choose(), number)

def botMove(number: int, botIQ: int) -> int:
    if(botIQ == 2):
        move = random. randrange(1, 29)
    else:
        if(number > 58):
            move = random. randrange(1, 29)
        else:
            move = botIAEnable(number)
    return move

def botIAEnable(number: int) -> int:
    count = 0
    if(number > 57):
        while(number > 57):
            count += 1
            number -= 1
            if(count == 29):
                count -= 1
                break
    elif(57 > number > 29):
        while(number > 29):
            count += 1
            number -= 1
            if(count == 29):
                count -= 1
                break
    else:
        count = number
    return count


typeOfGame(modeChoose())
