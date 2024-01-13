import pyautogui
import time
import keyboard

for i in range(100):
    if keyboard.is_pressed('g'):  # if key 'g' is pressed
        print('You Pressed A Key!')
        break  # finish the loop
    else:
        if pyautogui.mouseDown():  # if mouse is held down
            x, y = pyautogui.position()  # get current mouse position
            pyautogui.click(x, y)  # click at current mouse position
            time.sleep(0.1)
