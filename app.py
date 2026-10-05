from storage import load_file, save_file
from viwe import show_collection
from utils import check_confirm
from core import delete_task, add_task, edit_task
from config import NAME_FILE_SAVES
from utils import insure_saves_file
name_file = 'saves.txt'

"""главный цик приложения"""
def app():
    is_running = True
    name_file = NAME_FILE_SAVES
    insure_saves_file(name_file)
    task_collection = load_file([], name_file)
    while is_running:
        print("Меню\n"
            "1 - показать задачи\n"
            "2 - добавить заметку\n"
            "3 - Редактировать задачу\n"
            "4 - Удалить задачу\n"
            "5 - выйти\n")
        choice_user = input('ВВедите ваш выбор (1,2,3,4 или 5)')



        match str(choice_user):
            case '1':
                show_collection(task_collection)
                input("Нажмите 'ENTER' чтобы продолжить")
            case '2':
                task_collection = add_task(task_collection)
                print(task_collection)
                save_file(task_collection, name_file)
            case '3':
                show_collection(task_collection)
                task_collection = edit_task(task_collection)
                save_file(task_collection, name_file)

            case '4':
                show_collection(task_collection)
                task_collection = (task_collection)
                save_file(task_collection, name_file)

            case '5':
                is_running = False
                print("Пока-пока")

            case _:
                print('Такого пункста нет')