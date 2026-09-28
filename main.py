"""Основной файл приложения Task Manager
    version 0.0.5
    внесения:
    исправление ошибок
    оптимизация
    приложение может:
    сохранять задачу, редактировать
    и может удалять задачу.
"""

is_running = True #flag
name_file = 'saves.txt'

def show_collection(task_collection):
    print("-" * 30)
    for number, content in enumerate(task_collection):
        word = ''
        for symbol in content:
            if symbol == '|':
                word = f"{word}{symbol}"
            else:
                break
        print(number + 1, str(word))
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
    task_name = input("Введите имя задачи для добавления")
    task_content = input("Введите содержание задачи")
    if task_name.startswith('') or task_content.startswith(''):
        if len(task_content) < 2 and len(task_content) < 2:
            print(f"Имя задачи и содержание не должнео быть пустым !")
            return
    else:
        full_name = f"{task_name} | {task_content}"
        task_collection.append(full_name)

def load_file(task_list, file_name):
    name_file = "saves.txt"
    with open(name_file, "r", encoding="utf-8") as file:
        for line in file:
            task_list.append(line)

"""сохранение списка задач в файл"""
def save_file(task_list, file_name):
    with open(name_file, "w", encoding="utf-8") as file:
        for line in task_list:
            file.write(f"{line}")

"""главный цик приложения"""
def main():
    global is_running
    global name_file
    while is_running:
        print("Меню\n"
            "1 - показать задачи\n"
            "2 - добавить заметку\n"
            "3 - Редактировать задачу\n"
            "4 - Удалить задачу\n"
            "5 - выйти\n")
        choice_user = input('ВВедите ваш выбор (1,2,3,4 или 5)')
        task_collection = []

        load_file(task_collection, name_file)

        match str(choice_user):
            case '1':
                show_collection(task_collection)
                input("Нажмите 'ENTER' чтобы продолжить")
            case '2':
                add_task(task_collection)
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