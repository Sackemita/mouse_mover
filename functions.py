
import tkinter as tk

def utworzenie_okna():
    window = tk.Tk()  # utworzenie okna
    window.title("Hello World")

    label = tk.Label(window, text="Witaj Świecie")
    label.pack(side=tk.BOTTOM)
    tk.mainloop()

