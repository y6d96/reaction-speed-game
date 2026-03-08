# I acknowledge the use of ChatGPT (OpenAI) to help generate parts of this code.

import tkinter as tk
import random
import time

window = tk.Tk()
window.title("Reaction Speed Game")
window.geometry("400x300")

# Game title label
label = tk.Label(window, text="Reaction Speed Game", font=("Arial", 20))
label.pack(pady=40)

start_time = 0

def start_game():
    window.after(random.randint(2000, 5000), show_green)

def show_green():
    global start_time
    label.config(text="CLICK NOW!", bg="green")
    start_time = time.time()
# START BUTTON (add it here)
start_button = tk.Button(window, text="Start")
start_button.pack()

window.mainloop()