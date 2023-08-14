# Задача 34:  Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”,
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам

def check_the_rhythm(poem):
    count_a = list()
    for i in range(len(poem)):
        total = 0
        for j in range (len(poem[i])):
            if poem[i][j] =="а":
                total+=1
        count_a.append(total)
    return count_a

# нагуглила что можно и так, но сама не додумалась до этого
def check_the_rhythm(poem):
    count_a = list(map(lambda x: x.count("а"), poem))
    return count_a

# а эту не понимаю как сократить и нагуглить не могу. гпт чат предлагает слишком сложно как-то
def pro (count_a):
    for i in range(len(count_a)-1):
        if count_a[i] == count_a[i+1]:
            return "Парам пам-пам"
        return "Пам парам" 

poem = "пара-раа-рам рам-пам-папам па-ра-па-да".split(' ')
print(pro(check_the_rhythm(poem)))