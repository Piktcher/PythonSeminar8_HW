def addContacts():
    with open('contacts.txt', 'a') as book:
        print("\nВведите Фамилию И.О. нового контакта: ", end='')
        book.write(input() + " ")
        print("\nВведите номер телефона добавленного контакта: ", end='')
        book.write(input() + '\n')
        print("\nКонтакт успешно добавлен!")

        book.close

def getContacts():
    with open('contacts.txt', 'r') as book:
        print(f'\nПеречень всех контактов:\n{book.read()}')

        book.close

def searchContactID():
    print("\nВведите фамилию контакта: ", end='')
    second_name = input()
    with open('contacts.txt', 'r') as book:
        results = 0
        for i in book.readlines():
           if i.find(second_name) != -1:
               print(f'\nНайден контакт: {i}')
               results += 1
        if results == 0:
            print("\nТакие контакты не найдены, попробуйте еще раз!")
        book.close

def changeContacts():
    print("\nВведите фамилию или телефон контакта для изменения: ", end='')
    data = input()
    with open('contacts.txt', 'r') as book:
        file = book.readlines()
        res = False
        for i in range(len(file)):
            if data in file[i]:
                print("\nВведите новые данные ФИО и телефона для контакта")
                new_fio = input("\nФИО: ")
                new_phone = input("Телефон: ")
                file[i] = new_fio + " " + new_phone
                res = True
        if res == False:
            return print("\nТакой контакт не найден")
        book.close
    with open('contacts.txt', 'w') as book_1:
        book_1.write("".join(file))
        book_1.close
    print("\nКонтакт изменен")

def deleteContacts():
    print("\nВведите фамилию или телефон контакта для удаления: ", end='')
    data = input()
    with open('contacts.txt', 'r') as book:
        file = book.readlines()
        res = False
        for i in range(len(file)):
            if data in file[i]:
                file.remove(file[i])
                res = True
        if res == False:
            return print("\nТакой контакт не найден")
        book.close
    with open('contacts.txt', 'w') as book_1:
        book_1.write("".join(file))
        book_1.close
    print("\nКонтакт удален")