import tkinter as tk #test
from tkinter import filedialog, messagebox
import subprocess

class FileProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Обработчик файлов")

        self.input_file_label = tk.Label(root, text="Выберите основной файл:")
        self.input_file_label.pack(pady=5)

        self.input_file_entry = tk.Entry(root, width=50)
        self.input_file_entry.pack(pady=5)

        self.input_file_button = tk.Button(root, text="Обзор...", command=self.select_input_file)
        self.input_file_button.pack(pady=5)

        self.base_file_label = tk.Label(root, text="Выберите базовый файл:")
        self.base_file_label.pack(pady=5)

        self.base_file_entry = tk.Entry(root, width=50)
        self.base_file_entry.pack(pady=5)

        self.base_file_button = tk.Button(root, text="Обзор...", command=self.select_base_file)
        self.base_file_button.pack(pady=5)

        self.checkbox_frame = tk.Frame(root)
        self.checkbox_frame.pack(pady=10)

        self.checkbox1_var = tk.IntVar()
        self.checkbox1 = tk.Checkbutton(self.checkbox_frame, text="Создать tlocation с FA", variable=self.checkbox1_var)
        self.checkbox1.pack(side=tk.LEFT, padx=10)

        self.checkbox2_var = tk.IntVar()
        self.checkbox2 = tk.Checkbutton(self.checkbox_frame, text="Создать лист со статистикой", variable=self.checkbox2_var)
        self.checkbox2.pack(side=tk.LEFT, padx=10)

        self.process_button = tk.Button(root, text="Обработать файлы", command=self.process_files)
        self.process_button.pack(pady=20)

    def select_input_file(self):
        file_path = filedialog.askopenfilename(title="Выберите основной Excel файл", filetypes=[("Excel файлы", "*.xlsx")])
        if file_path:
            self.input_file_entry.delete(0, tk.END)
            self.input_file_entry.insert(0, file_path)

    def select_base_file(self):
        file_path = filedialog.askopenfilename(title="Выберите базовый Excel файл", filetypes=[("Excel файлы", "*.xlsx")])
        if file_path:
            self.base_file_entry.delete(0, tk.END)
            self.base_file_entry.insert(0, file_path)

    def process_files(self):
        input_file_path = self.input_file_entry.get()
        base_file_path = self.base_file_entry.get()

        if not input_file_path:
            messagebox.showerror("Ошибка", "Выберите основной файл!")
            return

        checkbox1_checked = self.checkbox1_var.get() == 1
        checkbox2_checked = self.checkbox2_var.get() == 1

        if checkbox1_checked and checkbox2_checked:
            if not base_file_path:
                messagebox.showerror("Ошибка", "Выберите базовый файл!")
                return
            self.process_with_both_options(input_file_path, base_file_path)
        elif checkbox1_checked:
            if not base_file_path:
                messagebox.showerror("Ошибка", "Выберите базовый файл!")
                return
            self.process_create_tlocation_with_fa(input_file_path, base_file_path)
        elif checkbox2_checked:
            tlocation_path = filedialog.askopenfilename(title="Выберите файл tlocation", filetypes=[("Excel файлы", "*.xlsx")])
            if tlocation_path:
                self.process_create_statistics(tlocation_path)
        else:
            messagebox.showerror("Ошибка", "Выберите хотя бы один чекбокс!")

    def process_with_both_options(self, input_file_path, base_file_path):
        result = subprocess.run(["python", "main.py", input_file_path, base_file_path, "--both"], capture_output=True, text=True)
        if result.returncode == 0:
            messagebox.showinfo("Успех", "Файлы успешно обработаны!")
        else:
            messagebox.showerror("Ошибка", f"Произошла ошибка:\n{result.stderr}")

    def process_create_tlocation_with_fa(self, input_file_path, base_file_path):
        result = subprocess.run(["python", "main.py", input_file_path, base_file_path, "--tlocation"], capture_output=True, text=True)
        if result.returncode == 0:
            messagebox.showinfo("Успех", "Файл tlocation успешно создан с FA!")
        else:
            messagebox.showerror("Ошибка", f"Произошла ошибка:\n{result.stderr}")

    def process_create_statistics(self, tlocation_path):
        result = subprocess.run(["python", "main.py", tlocation_path, "--statistics"], capture_output=True, text=True)
        if result.returncode == 0:
            messagebox.showinfo("Успех", "Лист со статистикой успешно создан!")
        else:
            messagebox.showerror("Ошибка", f"Произошла ошибка:\n{result.stderr}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileProcessorApp(root)
    root.mainloop()
