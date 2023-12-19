import pyautogui
import time
time.sleep(2)
for i in range(500):
    time.sleep(1)
    pyautogui.typewrite("Your Text Here")
    pyautogui.press('enter')
