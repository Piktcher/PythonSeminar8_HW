def start():
    print("Добрый день, как Вас зовут?")
    name = input("\n---")

    print(f"\nОчень приятно, {name}!")

def action():
    import file_func
    print("\nВам доступно несколько действий со списком контактов:\n1 - Добавить новый контакт\n2 - Вывести все контакты\n3 - Найти контакт\n4 - Изменить контакт\n5 - Удалить контакт\n0 - Выйти из приложения")
    while True:
        print("\nВведите номер действия и нажмите ввод: ", end='')
        action = int(input())
        if action == 1:
            file_func.addContacts()
        elif action == 2:
            file_func.getContacts()
        elif action == 3:
            file_func.searchContactID()
        elif action == 4:
            file_func.changeContacts()
        elif action == 5:
            file_func.deleteContacts()
        elif action == 0:
            print("\nДо свидания!")
            exit()
        else:
            print("\nВ следующий раз выберите значение из списка")