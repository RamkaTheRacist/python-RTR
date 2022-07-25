#Напишите программу, удаляющую из текста все слова, содержащие "абв".
word = 'абв Ура, питон круто, очеагбвнь инетресные семинарабвы! абв'
string = word.split()
res = list(filter(lambda x:'абв' not in x, string))
result = ''
for i in range(len(res)):
    result += f'{res[i]} '
print(result)