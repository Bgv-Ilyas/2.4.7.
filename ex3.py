import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    filename = entry.get()
    if filename:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
            text.delete(1.0, tk.END)
            text.insert(tk.END, content)
        except FileNotFoundError:
            messagebox.showerror("Ошибка", f"Файл '{filename}' не найден")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    else:
        messagebox.showerror("Ошибка", "Пожалуйста, укажите имя файла")

def save_file():
    filename = entry.get()
    if filename:
        content = text.get(1.0, tk.END)
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(content)
            messagebox.showinfo("Успех", f"Файл '{filename}' успешно сохранен")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    else:
        messagebox.showerror("Ошибка", "Пожалуйста, укажите имя файла")

# Создаем главное окно
root = tk.Tk()
root.title("Текстовый редактор")

# Однострочное текстовое поле для ввода имени файла
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Многострочное текстовое поле для содержимого файла
text = tk.Text(root, wrap='word', width=80, height=20)
text.pack(padx=10, pady=10)

# Кнопка "Открыть"
open_button = tk.Button(root, text="Открыть", command=open_file)
open_button.pack(side=tk.LEFT, padx=10, pady=10)

# Кнопка "Сохранить"
save_button = tk.Button(root, text="Сохранить", command=save_file)
save_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Запуск главного цикла приложения
root.mainloop()
