import tkinter as tk
from datetime import datetime

def update__time():
    current__time = datetime.now().strftime("%H:%M:%S")
    clock__label.config(text=current__time)
    clock__label.after(1000, update__time)

root = tk.Tk()
root.title("Fabulous Clock")

clock__label = tk.Label(root, font=("Elephant", 80), fg= "black", bg="pink")

clock__label.pack(fill="both", expand=True)

update__time()
root.mainloop()
