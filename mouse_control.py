# Developed by MD-Nazmus Samin Sunbeam
# Script used to test mouse controls
# https://pyautogui.readthedocs.io/en/latest/mouse.html
import pyautogui, sys

print("Screen Resolution Size: ", pyautogui.size())
print("Mouse Cursor Position: ", pyautogui.position())

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')