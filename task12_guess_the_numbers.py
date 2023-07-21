# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.


numSum = int(input("The sum of this two numbers:"))
numProduct = int(input("The product of this two numbers:"))
problem_solved = False
resultList=[]
for i in range(1, 1001):
    j=numSum-i
    if i*j==numProduct:
        resultList.append((i,j))
        problem_solved=True
    i+=1
if not problem_solved:
    print("Ooops! Solution doesn't exist")
print(*resultList)

#  2 вариант:

numSum = int(input("The sum of this two numbers:"))
numProduct = int(input("The product of this two numbers:"))
problem_solved = False

for num1 in range(1, 1001):
    for num2 in range(1, 1001):
        if (num2+num1==numSum) and (num2*num1==numProduct):
            print (num1,num2) 
            problem_solved = True
        else: num2+=1
    num1+=1

if not problem_solved:
    print ("ooops")
