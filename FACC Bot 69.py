# Fully Automatic Comment Creator Bot 69
from tkinter import *
import pyautogui

root = Tk()
root.title('FACC Bot 69')
root.configure(background='gray27')
root.iconbitmap('c:/Users/cresr/Downloads/covid-19.ico.ico')

entry_screen = Entry(root, width=35, borderwidth=5)
entry_screen.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

# inserting value
def number_value(number):
    current = entry_screen.get()
    entry_screen.delete(0, END)
    entry_screen.insert(0, str(current) + str(number))

# clear button
def clear_value():
    entry_screen.delete(0, END)

# keyboard controller
def new_value():
    i = entry_screen.get()
    i = int(i)
    x = 0
    pyautogui.hotkey('alt', 'tab')
    while i > x:
        pyautogui.write("a")
        pyautogui.press('enter')
        x += 1

# button function
button_quit = Button(root, text="Stop", padx=45, pady=20, command=root.quit)
start_button = Button(root, text="Start", padx=40, pady=20, command=new_value)
clear_button = Button(root, text="Clear", padx=40, pady=20, command=clear_value)
btn_7 = Button(root, text="7", padx=40, pady=20, command=lambda: number_value(7))
btn_8 = Button(root, text="8", padx=40, pady=20, command=lambda: number_value(8))
btn_9 = Button(root, text="9", padx=40, pady=20, command=lambda: number_value(9))
btn_4 = Button(root, text="4", padx=40, pady=20, command=lambda: number_value(4))
btn_5 = Button(root, text="5", padx=40, pady=20, command=lambda: number_value(5))
btn_6 = Button(root, text="6", padx=40, pady=20, command=lambda: number_value(6))
btn_1 = Button(root, text="1", padx=40, pady=20, command=lambda: number_value(1))
btn_2 = Button(root, text="2", padx=40, pady=20, command=lambda: number_value(2))
btn_3 = Button(root, text="3", padx=40, pady=20, command=lambda: number_value(3))
btn_0 = Button(root, text="0", padx=40, pady=20, command=lambda: number_value(0))

# button position
start_button.grid(row=1, column=0, columnspan=2)
button_quit.grid(row=1, column=1, columnspan=2)
clear_button.grid(row=5, column=1, columnspan=2)
btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)
btn_4.grid(row=3, column=0)
btn_5.grid(row=3, column=1)
btn_6.grid(row=3, column=2)
btn_1.grid(row=4, column=0)
btn_2.grid(row=4, column=1)
btn_3.grid(row=4, column=2)
btn_0.grid(row=5, column=0)

root.mainloop()