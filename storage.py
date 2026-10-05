"""модуль который загружает и сохраняет"""

def load_file(task_list, file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            task_list.append(line.strip())
        return task_list

"""сохранение списка задач в файл"""
def save_file(task_list, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for line in task_list:
            file.write(f"{line}")