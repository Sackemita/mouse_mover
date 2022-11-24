from tkinter import Tk, Label, Button
import pyautogui

def utworzenie_okna():
    window = Tk()  # utworzenie okna
    window.title("Mouse Mover owo")
    window.geometry("800x600")

    label = Label(window, text="Mouse Mover", font=25, fg="pink")  #tekst górny
    label.pack()
    #window.mainloop()

    def click_mousemover():  #funkcja która odpala się po kliknięciu buttona (ruszanie myszka)
        print("wow funkcja działa")

    click_button=Button(window, text="Ruszanie myszki", width=15, height=5, command=click_mousemover)
    click_button.pack()
    window.mainloop()
