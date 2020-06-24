# Fully Automatic Comment Creator Bot 69
from tkinter import *
import pyautogui

root = Tk()
root.title('FACC Bot 69')
root.configure(background='gray27')

# Entry screens
entry_screen_label = Label(root, text="Message")
entry_screen_label.grid(row=0, column=0)
entry_screen = Entry(root, width=35, borderwidth=5)
entry_screen.grid(row=0, column=1, columnspan=6, padx=10, pady=10)


entry_screen2_label = Label(root, text="# of Repeats")
entry_screen2_label.grid(row=1, column=0)
entry_screen2 = Entry(root, width=35, bd=5)
entry_screen2.grid(row=1, column=1, columnspan=6, padx=10)

# what is the text being executed
def string_value(string):
    current1 = entry_screen.get()
    entry_screen.delete(0, END)
    entry_screen.insert(0, str(current1) + str(string))

# how many times is the program going to run
def number_value(number):
    current = entry_screen2.get()
    entry_screen2.delete(0, END)
    entry_screen2.insert(0, str(current) + str(number))

# mode1: 1 group send
def new_value():
    string_val = entry_screen.get()
    repeats = entry_screen2.get()
    repeats = int(repeats)
    x = 0
    pyautogui.hotkey('alt', 'tab')
    pyautogui.write(string_val)
    while repeats > x:
        pyautogui.write(string_val)
        pyautogui.press('enter')
        x += 1
# mode2: individual word send
def new_value2():
    string_val = entry_screen.get()
    repeats = entry_screen2.get()
    repeats = int(repeats)
    lst_string_val = string_val.split()
    x = 0
    pyautogui.hotkey('alt', 'tab')
    pyautogui.write(lst_string_val[0])
    while repeats > x:
        for word in range(len(lst_string_val)):
            pyautogui.write(lst_string_val[word])
            pyautogui.press('enter')
        x += 1
#mode3: individual letter send
def new_value3():
    string_val = entry_screen.get()
    repeats = entry_screen2.get()
    repeats = int(repeats)
    lst_string_val = list(string_val)
    x = 0
    pyautogui.hotkey('alt', 'tab')
    pyautogui.write(lst_string_val[0])
    while repeats > x:
        for word in range(len(lst_string_val)):
            pyautogui.write(lst_string_val[word])
            pyautogui.press('enter')
        x += 1

# modes
mode1 = Button(root, text="Mode 1", padx=40, pady=20, command=new_value)
mode1.grid(row=2, column=0, columnspan=2)
mode2 = Button(root, text="Mode 2", padx=40, pady=20, command=new_value2)
mode2.grid(row=2, column=3, columnspan=2)
mode3 = Button(root, text="Mode 3", padx=40, pady=20, command=new_value3)
mode3.grid(row=2, column=6, columnspan=2)

root.mainloop()
