# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

totalCoins = int(input("Amount of coins:"))
from random import randint
array=[randint(0,1) for i in range(totalCoins)]
print(array)
sum0=0
sum1=0
i=0
for i in range(totalCoins):
    if array[i]==0:
        sum0+=1
    else: sum1+=1
    i+=1

if sum0<=sum1:
    print(f"{sum0} coins should be flipped")
else: print(f"{sum1} coins should be flipped")    