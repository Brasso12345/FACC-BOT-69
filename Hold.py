import pyautogui
x = 0
i = input() #number of times it needs to be repeated
i = int(i)
#pyautogui.moveTo(760, 745)
#pyautogui.click()
pyautogui.hotkey('alt', 'tab')
while i > x:
    pyautogui.write("a")
    pyautogui.press('enter')
    x += 1
print("done")