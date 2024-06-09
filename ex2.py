#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk

# Создаем главное окно
root = tk.Tk()
root.title("Цвета радуги")

# Словарь цветов с их кодами и названиями
colors = {
    "Красный": "#ff0000",
    "Оранжевый": "#ff7d00",
    "Желтый": "#ffff00",
    "Зеленый": "#00ff00",
    "Голубой": "#007dff",
    "Синий": "#0000ff",
    "Фиолетовый": "#7d00ff"
}

# Функция, которая обновляет текстовое поле и метку при нажатии на кнопку
def update_color(color_name):
    color_code = colors[color_name]
    color_code_entry.delete(0, tk.END)
    color_code_entry.insert(0, color_code)
    color_label.config(text=color_name)

# Создаем текстовое поле для отображения кода цвета
color_code_entry = tk.Entry(root, width=20)
color_code_entry.grid(row=0, column=0, columnspan=7)

# Создаем метку для отображения названия цвета
color_label = tk.Label(root, text="", font=("Helvetica", 16))
color_label.grid(row=1, column=0, columnspan=7)

# Создаем кнопки для каждого цвета радуги
row = 2
col = 0
for color_name, color_code in colors.items():
    btn = tk.Button(root, text=color_name, bg=color_code, command=lambda c=color_name: update_color(c))
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    col += 1

# Запуск главного цикла программы
root.mainloop()
