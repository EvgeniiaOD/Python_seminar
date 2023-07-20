# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
 
maxNumber = int (input("How far should we count to: "))
x=maxNumber
exponentsList = [2**i for i in range(x) if 2**i < maxNumber] 
print(f"Powers of 2: {exponentsList}") # не могу сообразить, как тут убрать скобки при выводе? если без f-сторки, то *exponentsList, а вот 

maxNumber = int (input("How far should we count to: "))
listExponents=[]
i=1
while 2**i < maxNumber:
    listExponents.append(2**i)
    i+=1
print(listExponents)    