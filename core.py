from utils import check_confirm
"""функция редактирование"""
def edit_task(task_collection):
    select_edit = input("Введите номер задачи: ")
    if check_confirm(delete_task, task_collection):
        edit_name = input("Новое имя задачи")
        task_collection[int(select_edit) - 1] = edit_name
        print(f"Задача {edit_name} успешно изменина!")

"""Функция удаления"""
def delete_task(task_collection):
    delete_task = input("Введите номер задачи для удаления")
    if check_confirm(delete_task, task_collection):
        task_collection.pop(int(delete_task) - 1)
        print(f"Задача под номером {delete_task} успешно удалена")

""""Функция добаления"""
def add_task(task_collection):
    task_name = input("Введите имя задачи для добавления")
    task_content = input("Введите содержание задачи")
    if task_name.startswith(' ') or task_content.startswith(' '):
        if len(task_content) < 2 and len(task_content) < 2:
            print(f"Имя задачи и содержание не должнео быть пустым !")
    else:
        full_name = f"{task_name} | {task_content}"
        task_collection.append(full_name)
        return task_collection
    return task_collection