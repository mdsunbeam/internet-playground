# Developed by MD-Nazmus Samin Sunbeam
# Script used to test taking a screenshot and showing it
# https://pyautogui.readthedocs.io/en/latest/screenshot.html
import pyautogui
import matplotlib.pyplot as plt

im1 = pyautogui.screenshot()

imgplot = plt.imshow(im1)

plt.show()