import tkinter as tk

def update_label():
    selected_value = radio_var.get()
    label.config(text=f"Вы выбрали: {selected_value}")

# Создаем главное окно
root = tk.Tk()
root.title("Radiobuttons as Buttons")

# Переменная для хранения значения выбранной радиокнопки
radio_var = tk.StringVar(value="")

# Метка для отображения информации
label = tk.Label(root, text="Выберите опцию", font=("Helvetica", 14))
label.pack(pady=10)

# Список опций
options = ["Опция 1", "Опция 2", "Опция 3"]

# Создаем радиокнопки с indicatoron=0
for option in options:
    rb = tk.Radiobutton(root, text=option, value=option, variable=radio_var, 
                        indicatoron=0, command=update_label, width=15, font=("Helvetica", 12))
    rb.pack(pady=5)

# Запуск главного цикла приложения
root.mainloop()
