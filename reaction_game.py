# I acknowledge the use of ChatGPT (OpenAI) to help generate parts of this code.

import tkinter as tk
import random
import time

window = tk.Tk()
window.title("Reaction Speed Challenge")
window.geometry("400x300")
window.configure(bg="lightyellow")

start_time = 0
waiting_for_green = False
waiting_for_click = False
after_id = None

label = tk.Label(window, text="Reaction Speed Game", font=("Arial", 22), bg="white")
label.pack(pady=40)

result_label = tk.Label(window, text="", font=("Arial", 12), bg="lightyellow")
result_label.pack()

def start_game():
    global waiting_for_green, waiting_for_click, after_id

    label.config(text="Wait for green...", bg="white")
    result_label.config(text="")

    waiting_for_green = True
    waiting_for_click = False

    delay = random.randint(2000, 5000)
    after_id = window.after(delay, show_green)

def show_green():
    global start_time, waiting_for_green, waiting_for_click

    label.config(text="CLICK NOW!", bg="green")

    start_time = time.time()
    waiting_for_green = False
    waiting_for_click = True

def click_screen(event):
    global waiting_for_green, waiting_for_click, after_id

    if waiting_for_green:
        window.after_cancel(after_id)
        label.config(text="Too Soon! Click Start to try again.", bg="red")
        waiting_for_green = False

    elif waiting_for_click:
        reaction = round((time.time() - start_time) * 1000)
        label.config(text=f"Reaction time: {reaction} ms", bg="white")
        result_label.config(text="Click Start to play again")
        waiting_for_click = False

start_button = tk.Button(window, text="Start", font=("Arial", 12), command=start_game)
start_button.pack(pady=10)

window.bind("<Button-1>", click_screen)

window.mainloop()