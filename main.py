"""Основной файл приложения Task Manager
    version 0.0.3
    -[x] сделать функцию - редактирование заметок
    -[x] сделать функции - удаления заметок
"""

collection = ['task 1', 'task 2'] #Лист
is_start = True #flag

while (is_start):
    print("Меню"
        "1 - показать задачи\n"
        "2 - добавить заметку\n"
        "3 - Редактировать задачу\n"
        "4 - Удалить задачу\n"
        "5 - выйти\n")
    choice_user = input('ВВедите ваш выбор (1,2,3,4 или 5)')

    match choice_user:
        case '1':
            print(collection)
        case '2':
            collection.append('task')
            print(collection)
        case '3':
            select_edit = int(input("Введите номер задачи: "))
            edit_name = input("Введите новое имя задачи: ")
            collection[select_edit - 1] = edit_name
            print(collection)

        case '4':
            delete_edit = int(input("Введите номер задачи: "))
            collection.pop(delete_edit - 1)
            print(collection)

        case '5':
            is_start = False
            print("Пока-пока")

        case _:
            print('Такого пункста нет')