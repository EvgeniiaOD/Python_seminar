# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения 
# и удаления данных

def show_menu(): #возвращает переменую choice (число)
    print('1. Распечатать справочник\n'     
    '2. Найти телефон по фамилии\n'
    '3. Изменить номер телефона\n'
    '4. Удалить запись \n'
    '5. Найти абонента по номеру телефона \n'
    '6. Добавить абонента в справочник \n'  
    '7. Закончить работу \n')
    choice=int(input("Что делаем? "))
    return choice

def read_txt(): # возвращает phone_book (словарь картежей)
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open ('phonebook.csv' , 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    return phone_book


phone_book = read_txt()
print(f"распечатка рид_ткст: {phone_book}\n") #тест функции рид_текст

def write_txt(filename,phone_book): #сохранение данных в файл?  
    with open('phonebook.csv','w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s+=v+','
                phout.write(f'{s[:-1]}\n')

def print_result(phone_book): #вывод записной книжки на печать
    for item in phone_book:
        print("Фамилия:", item['Фамилия'])
        print("Имя:", item['Имя'])
        print("Телефон:", item['Телефон'])
        print("Описание:", item['Описание'])
        print()
  
print_result(phone_book) #тест функции принт_резалт 

def find_by_lastname(phone_book): #Ищет + выводит пользователя по фамилии
    lastname = input("Введите фамилию: ")
    for item in phone_book:
        if item['Фамилия'] == lastname:
            print("Фамилия:", item['Фамилия'])
            print("Имя:", item['Имя'])
            print("Телефон:", item['Телефон'])
            print("Описание:", item['Описание'])
            print()
        elif item['Имя'] == lastname:
            print("Фамилия:", item['Фамилия'])
            print("Имя:", item['Имя'])
            print("Телефон:", item['Телефон'])
            print("Описание:", item['Описание'])
            print()
            break
        elif item['Телефон'] == lastname:
            print("Фамилия:", item['Фамилия'])
            print("Имя:", item['Имя'])
            print("Телефон:", item['Телефон'])
            print("Описание:", item['Описание'])
            print()
            break

find_by_lastname(phone_book) #тест функции файнд_бай_ластнэйм
    

def change_number(phone_book): #заменяет номер + выводит обновленный контакт
    last_name = input("Введите фамилию: ")
    new_number = input("Введите номер: ")
    for item in phone_book:
        if item['Фамилия'] == last_name:
            item ['Телефон'] = new_number
            print("Фамилия:", item['Фамилия'])
            print("Имя:", item['Имя'])
            print("Телефон:", item['Телефон'])
            print("Описание:", item['Описание'])
            print()
            break

change_number(phone_book) #тест функции чендж_намбер


def delete_by_lastname (phone_book):
    lastname = input("Введите фамилию для удаления : ")
    for item in phone_book:
        # count=0
        if item['Фамилия'] == lastname:
            # del phone_book[count]
            del item ['Фамилия']
            del item['Имя']
            del item['Телефон']
            del item['Описание']
        elif item['Имя'] == lastname: 
            del item ['Фамилия']
            del item['Имя']
            del item['Телефон']
            del item['Описание']
        # else: count+=1
    return phone_book

print(delete_by_lastname (phone_book)) #тест функции делит_бай_ластнэйм


def find_by_number (phone_book):
    number = input("Введите номер: ")
    for item in phone_book:
        if item ['Телефон'] == number:
            print("Фамилия:", item['Фамилия'])
            print("Имя:", item['Имя'])
            print("Телефон:", item['Телефон'])
            print("Описание:", item['Описание'])
            print()

find_by_number (phone_book)

def add_user (phone_book): #недописана и пока не знаю как дописать 
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    last_name = input("Введите фамилию: ")
    first_name= input("Введите имя: ")
    number = input("Введите телефон: ")
    comment=input("Введите описание: ")
    user_data=[last_name, first_name, number, comment]
    for item in user_data:
        new_user = dict(zip(fields, user_data[item]))
        phone_book.append(new_user)
    return phone_book

print(add_user(phone_book))


def work_with_phonebook():
    choice=show_menu()

    phone_book=read_txt('phonebook.csv')

    while (choice!=7):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new number ')
            print(change_number(phone_book,last_name,new_number))
        elif choice==4:
            lastname=input('lastname ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_data=input('new data ')
            add_user(phone_book,user_data)
            write_txt('phonebook.csv',phone_book)

choice=show_menu()

