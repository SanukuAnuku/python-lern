"""Основной файл приложения Task Manager
    version 0.1.0
    создание exe файла
    приложение может:
    добавление котента задач
    сохранять задачу, редактировать
    и может удалять задачу.
"""
from core import TaskManager


if __name__ == '__main__':
    app = TaskManager()
    app.run()
