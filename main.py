"""Основной файл приложения Task Manager
    version 0.0.2
    -[] реализовать место хранения задачь
    -[] сделать функцию - показать заметки
    -[] сделать функцию - добавить заметки
"""
collection = ['task 1', 'task 2'] #Лист
is_start = True #flag

while (is_start):
    print("1 - показать задачи | 2 - добавить заметку")
    choice_user = input('ВВедите ваш выбор (1 или 2)')

    match choice_user:
        case '1':
            print(collection)
        case '2':
            collection.append('task')
            print(collection)
        case _:
            print('Такого пункста нет')
