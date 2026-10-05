""""Проверка"""
import os
import sys



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

def get_base_dir():
    if getattr(sys, 'frozen', False):
      return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.realpath(__file__))

def insure_saves_file(name_file):
    if not os.path.exists(name_file):
        with open(name_file, "w") as f:
            f.write("")

