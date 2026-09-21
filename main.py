"""Основной файл приложения Task Manager
    version 0.0.5
    внесения:
    исправление ошибок
    оптимизация
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

def check_confirm(select_task, task_list):
    if select_task.isdigit():
        if (int(select_task) > 0 and int(select_task) <= len(task_list)):
            return True
        else:
            print(f"Задача с номером {select_task} нет в списке")
            return False
    else:
        print(f"Введите миенно номер задачи!")
        return False

def edit_task(task_collection):
    select_edit = input("Введите номер задачи: ")
    if check_confirm(delete_task, task_collection):
        edit_name = input("Новое имя задачи")
        task_collection[int(select_edit) - 1] = edit_name
        print(f"Задача {edit_name} успешно изменина!")

def delete_task(task_collection):
    delete_task = input("Введите номер задачи для удаления")
    if check_confirm(delete_task, task_collection):
        task_collection.pop(int(delete_task) - 1)
        print(f"Задача под номером {delete_task} успешно удалена")

def add_task(task_collection):
    add_task = input("Введите имя задачи для добавления")
    if add_task.startswith('  '):
        if len(add_task) < 2:
            print("Название не может быть пустым!")
        else:
            print("")
    else:
        collection.append(add_task)
        print(collection)


def main():
    global is_running
    while is_running:
        print("Меню\n"
            "1 - показать задачи\n"
            "2 - добавить заметку\n"
            "3 - Редактировать задачу\n"
            "4 - Удалить задачу\n"
            "5 - выйти\n")
        choice_user = input('ВВедите ваш выбор (1,2,3,4 или 5)')

        name_file = "saves.txt"
        file = open(name_file, "r", encoding="utf-8")
        for line in file:
            task_collection.append(line.split(''))
            print(line)

        match str(choice_user):
            case '1':
                show_collection(task_collection)
                input("Нажмите 'ENTER' чтобы продолжить")
            case '2':
                add_task(task_collection)
                name_file = "saves.txt"
                file = open(name_file, "w", encoding="utf-8")
                for line in task_collection:
                    file.write(f"{task}\n")
            case '3':
                show_collection(task_collection)
                edit_task(task_collection)

            case '4':
                show_collection(task_collection)
                delete_task(task_collection)

            case '5':
                is_running = False
                print("Пока-пока")

            case _:
                print('Такого пункста нет')

if __name__ == "__main__":
    main()