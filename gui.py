import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import re
import os

# Функция для создания нового Excel файла
def create_new_excel(input_file):
    # Здесь ваш код для создания нового Excel файла
    # Например:
    output_file = 'output.xlsx'
    df = pd.read_excel(input_file)
    df.to_excel(output_file, index=False)
    return output_file

# Функция для сортировки данных в Excel файле
def sort_excel(file):
    # Здесь ваш код для сортировки данных в Excel файле
    # Например:
    df = pd.read_excel(file)
    df_sorted = df.sort_values(by=['column_to_sort_by'])
    df_sorted.to_excel(file, index=False)

# Функция для обработки данных в зависимости от выбранных опций
def process_data():
    input_file = file_path.get()
    if not input_file:
        messagebox.showerror("Ошибка", "Выберите файл Excel")
        return
    
    if create_file.get() and sort_file.get():
        messagebox.showerror("Ошибка", "Выберите только одну опцию")
        return
    
    if create_file.get():
        output_file = create_new_excel(input_file)
        messagebox.showinfo("Успешно", f"Создан новый файл: {output_file}")
    elif sort_file.get():
        sort_excel(input_file)
        messagebox.showinfo("Успешно", "Данные в файле отсортированы")

# Функция для выбора файла
def choose_file():
    file_path.set(filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")]))

# Создание основного окна приложения
root = tk.Tk()
root.title("Обработка Excel файлов")

# Переменная для хранения пути к выбранному файлу
file_path = tk.StringVar()

# Фрейм для выбора файла
file_frame = tk.Frame(root)
file_frame.pack(pady=20)

tk.Button(file_frame, text="Выбрать файл", command=choose_file).pack()

# Фрейм для выбора опций
options_frame = tk.Frame(root)
options_frame.pack(pady=20)

create_file = tk.IntVar()
sort_file = tk.IntVar()

tk.Checkbutton(options_frame, text="Создать новый файл", variable=create_file).grid(row=0, column=0, padx=20)
tk.Checkbutton(options_frame, text="Сортировать файл", variable=sort_file).grid(row=0, column=1, padx=20)

# Кнопка для обработки данных
tk.Button(root, text="Обработать данные", command=process_data).pack()

root.mainloop()
