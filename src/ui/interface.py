import json
import tkinter as tk
from pathlib import Path


class Interface:
    def __init__(self, windows_w=500, windows_h=400):
        # Главное окно приложения
        self.root = tk.Tk()
        self.root.title("Task Manager")
        self.root.geometry(f"{windows_w}x{windows_h}")
        self.root.configure(bg="#202020")
        self.root.minsize(400, 300)

        self.tasks_file = Path(__file__).resolve().parents[1] / "task.json"
        self.tasks = []

        self.create_interface()
        self.load_tasks()

    def create_interface(self):
        self.title_label = tk.Label(
            self.root, text="TASK MANAGER", font=("Arial", 18, "bold"),
            bg="#202020", fg="white"
        )
        self.title_label.pack(pady=12)

        self.entry = tk.Entry(self.root, font=("Arial", 12))
        self.entry.pack(fill="x", padx=20, pady=5)
        self.entry.bind("<Return>", self.add_task)

        self.task_list = tk.Listbox(
            self.root, font=("Arial", 11), bg="#303030", fg="white",
            selectbackground="#555555", height=12
        )
        self.task_list.pack(fill="both", expand=True, padx=20, pady=8)

        buttons = tk.Frame(self.root, bg="#202020")
        buttons.pack(pady=8)

        tk.Button(buttons, text="Добавить", command=self.add_task).pack(side="left", padx=4)
        tk.Button(buttons, text="Удалить", command=self.delete_task).pack(side="left", padx=4)
        tk.Button(buttons, text="Очистить", command=self.clear_entry).pack(side="left", padx=4)

    def load_tasks(self):
        if self.tasks_file.exists():
            try:
                with open(self.tasks_file, "r", encoding="utf-8") as file:
                    data = json.load(file)
                if isinstance(data, list):
                    self.tasks = [str(task) for task in data]
            except (OSError, json.JSONDecodeError):
                self.tasks = []
        self.update_tasks()

    def save_tasks(self):
        try:
            with open(self.tasks_file, "w", encoding="utf-8") as file:
                json.dump(self.tasks, file, ensure_ascii=False, indent=4)
        except OSError as error:
            print(f"Не удалось сохранить задачи: {error}")

    def update_tasks(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task)

    def add_task(self, event=None):
        task = self.entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_tasks()
            self.save_tasks()
            self.entry.delete(0, tk.END)

    def delete_task(self):
        selected = self.task_list.curselection()
        if selected:
            self.tasks.pop(selected[0])
            self.update_tasks()
            self.save_tasks()

    def clear_entry(self):
        self.entry.delete(0, tk.END)