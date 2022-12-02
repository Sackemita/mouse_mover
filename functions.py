from tkinter import Tk, Label, Button
import time
#import pyautogui

def utworzenie_okna():
    window = Tk()  # utworzenie okna
    window.title("Mouse Mover owo")
    window.geometry("800x600")

    label = Label(window, text="Mouse Mover", font=25, fg="pink")  #tekst górny
    label.pack()
    #window.mainloop()

    def click_mousemover():  #funkcja która odpala się po kliknięciu buttona (ruszanie myszka)
        print("wow funkcja działa")

    def click_timer():
        print("timer działa")
        seconds=time.time()
        local_time=time.ctime(seconds)
        print("local time: ", local_time)

        # t=Timer(30.0, click_timer)
        # t.start()
        # t.stop()

    click_button_mouse_mover=Button(window, text="Ruszanie myszki", width=15, height=5, command=click_mousemover)
    click_button_timer=Button(window, text="Timer", width =15, height=5, command=click_timer)

    click_button_mouse_mover.pack()
    click_button_timer.pack()
    window.mainloop()
