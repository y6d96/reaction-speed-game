# I acknowledge the use of ChatGPT (OpenAI) to help generate parts of this code.

import tkinter as tk

window = tk.Tk()
window.title("Reaction Speed Game")
window.geometry("400x300")

# Game title label
label = tk.Label(window, text="Reaction Speed Game", font=("Arial", 20))
label.pack(pady=40)

# START BUTTON (add it here)
start_button = tk.Button(window, text="Start")
start_button.pack()

window.mainloop()