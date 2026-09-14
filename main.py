"""Основной файл приложения Task Manager
    version 0.0.4
    приложение может:
    сохранять задачу, редактировать
    и может удалять задачу.
"""


collection = [] #Лист
is_running = True #flag

def show_collection(task_collection):
    print("-" * 30)
    for i, j in enumerate(task_collection):
        print(i + 1, j)
    print("-" * 30)
    
while (is_running):
    print("Меню\n"
        "1 - показать задачи\n"
        "2 - добавить заметку\n"
        "3 - Редактировать задачу\n"
        "4 - Удалить задачу\n"
        "5 - выйти\n")
    choice_user = input('ВВедите ваш выбор (1,2,3,4 или 5)')

    match choice_user:
        case '1':
            show_collection(collection)
        case '2':
            add_task = input("Введите имя задачи для добавления")
            collection.append(add_task)
            print(collection)
        case '3':
            show_collection(collection)
            select_task = int(input("Введите номер задачи: "))
            edit_task = input("Введите новое имя задачи для редактирование ")
            collection[select_task - 1] = edit_task
            print(collection)
        case '4':
            show_collection(collection)
            delete_task = int(input("Введите номер задачи для удаления"))
            collection.pop(delete_task - 1)
            print(collection)

        case '5':
            is_running = False
            print("Пока-пока")

        case _:
            print('Такого пункста нет')


