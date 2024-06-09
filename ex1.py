#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        label_result.config(text=str(result))
    except ValueError:
        label_result.config(text="ошибка")
    except ZeroDivisionError:
        label_result.config(text="ошибка")

# Создаем главное окно
root = tk.Tk()
root.title("Простейший калькулятор")

# Создаем текстовые поля для ввода чисел
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

# Размещаем текстовые поля
entry1.grid(row=0, column=0, columnspan=2)
entry2.grid(row=1, column=0, columnspan=2)

# Создаем кнопки для арифметических операций
button_add = tk.Button(root, text='+', command=lambda: calculate('+'))
button_sub = tk.Button(root, text='-', command=lambda: calculate('-'))
button_mul = tk.Button(root, text='*', command=lambda: calculate('*'))
button_div = tk.Button(root, text='/', command=lambda: calculate('/'))

# Размещаем кнопки
button_add.grid(row=2, column=0)
button_sub.grid(row=2, column=1)
button_mul.grid(row=3, column=0)
button_div.grid(row=3, column=1)

# Создаем метку для отображения результата
label_result = tk.Label(root, text="Результат")
label_result.grid(row=4, column=0, columnspan=2)

# Запускаем главное событие
root.mainloop()
