# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

num = int(input("Number of elements for set№1:"))
set_1= set()
for i in range(num):
    set_1.add(int(input("input values:")))
print(*set_1)
num = int(input("Number of elements for set№2:"))
set_2= set()
for i in range(num):
    set_2.add(int(input("input values:")))
print(*set_2)

print(*set_1.intersection(set_2))



