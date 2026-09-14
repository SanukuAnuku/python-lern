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
            waite = input("Нажмите 'ENTER' чтобы продолжить")
        case '2':
            add_task = input("Введите имя задачи для добавления")
            if add_task.startswith('  '):
                if len(add_task) < 2:
                    print("Название не может быть пустым!")
                    continue
            else:
                collection.append(add_task)
                print(collection)
        case '3':
            show_collection(collection)
            select_task = input("Введите номер задачи: ")
            if int(select_task.isdigit()):
                if int(select_task) > 0 and int(select_task) <= len(collection):
                    edit_task = input("Введите новое имя задачи для редактирование ")
                    collection[int(select_task) - 1] = edit_task
                    print(collection)
                    print(f"задача '{int(select_task)}' '{int(edit_task)}' умпешно отредактирована!")
                else:
                    print("Задачи с таким номером нет")
            else:
                print("Задачи с таким номером нет")
        case '4':
            show_collection(collection)
            delete_task = input("Введите номер задачи для удаления")
            if int(delete_task.isdigit()):
                if int(delete_task) <= len(collection) and int(delete_task) > 0:
                    collection.pop(int(delete_task) - 1)
                    print(f"задача '{int(delete_task)}' успешно удалена !")
                    print(collection)
                else:
                    print("Задачи с таким номером нет")
            else:
                print("Задачи с таким номером нет")

        case '5':
            is_running = False
            print("Пока-пока")

        case _:
            print('Такого пункста нет')


