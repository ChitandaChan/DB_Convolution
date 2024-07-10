import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Функции для выполнения программ
def program1(convolution.py):
    print(f"Выполняется Program 1 с файлом: {convolution.py}")
    # Добавьте код для выполнения Program 1 здесь

def program2(sort.py):
    print(f"Выполняется Program 2 с файлом: {sort.py}")
    # Добавьте код для выполнения Program 2 здесь

# Функции для выбора файлов
def choose_file1():
    file_path1 = filedialog.askopenfilename()
    file_label1.config(text=file_path1)

def choose_file2():
    file_path2 = filedialog.askopenfilename()
    file_label2.config(text=file_path2)

# Функция для выполнения выбранных программ
def execute_programs():
    file_path1 = file_label1.cget("text")
    file_path2 = file_label2.cget("text")

    if checkbox_var1.get() and not file_path1:
        messagebox.showwarning("Предупреждение", "Пожалуйста, выберите файл для Program 1.")
        return

    if checkbox_var2.get() and not file_path2:
        messagebox.showwarning("Предупреждение", "Пожалуйста, выберите файл для Program 2.")
        return
    
    if checkbox_var1.get():
        program1(file_path1)
    if checkbox_var2.get():
        program2(file_path2)

# Создание главного окна
root = tk.Tk()
root.title("Программа с визуализацией")

# Переменные для чекбоксов
checkbox_var1 = tk.BooleanVar()
checkbox_var2 = tk.BooleanVar()

# Чекбоксы для выбора программ
checkbox1 = tk.Checkbutton(root, text="Program 1", variable=checkbox_var1)
checkbox1.pack()

# Метка и кнопка для выбора файла для Program 1
file_label1 = tk.Label(root, text="Файл для Program 1 не выбран")
file_label1.pack()
choose_button1 = tk.Button(root, text="Выбрать файл для Program 1", command=choose_file1)
choose_button1.pack()

checkbox2 = tk.Checkbutton(root, text="Program 2", variable=checkbox_var2)
checkbox2.pack()

# Метка и кнопка для выбора файла для Program 2
file_label2 = tk.Label(root, text="Файл для Program 2 не выбран")
file_label2.pack()
choose_button2 = tk.Button(root, text="Выбрать файл для Program 2", command=choose_file2)
choose_button2.pack()

# Кнопка для выполнения выбранных программ
execute_button = tk.Button(root, text="Выполнить", command=execute_programs)
execute_button.pack()
