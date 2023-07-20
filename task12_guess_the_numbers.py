# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.


# numSum = int(input("The sum of this two numbers:"))
# numProduct = int(input("The product of this two numbers:"))

# solution_found = False

# if numSum in range(2, 2001):
#     for num1 in range(1001):
#         for num2 in range(1001):
#             if num1 + num2 == numSum and num1 * num2 == numProduct:
#                 print(f"Peter's numbers are: {num1}, {num2}")
#                 solution_found = True
#                 break  
#         if solution_found:
#             break  
#     if not solution_found:
#         print("ooops! Solution doesn't exist")
# else:
#     print("One or both numbers don't meet the condition")

# полностью мой вариант, где я никак не могу понять как выводить строку print ("ooops! Solution doesn't exist"), 
# ТОЛЬКО если у задачи нет решения: 
#  
numSum = int(input("The sum of this two numbers:"))
numProduct = int(input("The product of this two numbers:"))
num1=1
num2=1
if numSum in range(2, 2001):
    for num1 in range(1001):
        for num2 in range(1001):
            if num1+num2 == numSum:
                if num1*num2 == numProduct:
                    print (f"Peter's numbers are: {num1}, {num2}")
            else: num2+=1       
        num1+=1
    print ("ooops! Solution doesn't exist")       
else: print("One or both numbers don't meet the condition")  