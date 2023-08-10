# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
array = [randint(0, 100) for i in range(15)]
print(array)

minimum = int(input("минимум диапазона:"))
maximum = int(input("мaксимум диапазона:"))

new_array = [] 


def find_index(minimum, maximum):
    for i in range(len(array)):  
        if array[i] >= minimum and array[i] <= maximum:
            new_array.append(i)
    return new_array  


new_array = find_index(minimum, maximum)

print(*new_array)

