""""Проверка"""

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