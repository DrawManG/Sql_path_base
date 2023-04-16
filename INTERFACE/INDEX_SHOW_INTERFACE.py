import sqlite3
import tkinter as tk
from tkinter import ttk
import os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Создаем текстовое поле и кнопку поиска
        self.search_entry = tk.Entry(self)
        self.search_entry.grid(row=0, column=0)
        self.search_button = tk.Button(self, text='Поиск', command=self.search)
        self.search_button.grid(row=0, column=1)
        self.button = tk.Button(root, text="Запустить скрипты", command=self.run_scripts)
        self.button.grid(row=0, column=2)

        # Создаем таблицу
        self.tree = ttk.Treeview(self, columns=('Name', 'Path'), show='headings')
        self.tree.column('Name', width=100)
        self.tree.column('Path', width=200)
        self.tree.heading('Name', text='Name')
        self.tree.heading('Path', text='Path')
        self.tree.grid(row=1, column=0, columnspan=3, sticky="nsew")

        # Выполняем начальный запрос к базе данных
        self.search()
        # Добавляем обработчик двойного щелчка на строки таблицы
        self.tree.bind("<Double-1>", self.open_file)

    def open_file(self, event):
        # Получаем информацию о выбранной строке
        item = self.tree.item(self.tree.selection()[0])
        path = item['values'][1]

        # Открываем файл в стандартном приложении для его типа
        os.startfile(path)

    def run_scripts(self):

        path = "C:/Users/DHOUSE/GitHub/2w/Sql_path_base/BASE/"
        os.remove(f'{path}data.db')
        os.system(f"python {path}INDEX_CREATE_BASE.py")
        os.system(f"python {path}INDEX_ADDING_TO_BASE.py")
        os.system(f"python {path}INDEX_CREATE_TABLE_IN_BASE.py")

    def search(self):
        # Получаем строку поиска из текстового поля
        search_str = self.search_entry.get()

        # Выполняем запрос к базе данных
        with sqlite3.connect('C:/Users/DHOUSE/GitHub/2w/Sql_path_base/BASE/data.db') as conn:
            c = conn.cursor()
            c.execute("SELECT namefile, pathfile FROM Pather WHERE namefile LIKE ?", ('%' + search_str + '%',))
            rows = c.fetchall()

        # Очищаем таблицу и добавляем данные
        self.tree.delete(*self.tree.get_children())
        for row in rows:
            self.tree.insert('', 'end', values=row)

# Создаем окно
root = tk.Tk()
app = Application(master=root)
app.mainloop()
