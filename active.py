#! python3
"""Moves the mouse and clicks to prevent screen from sleeping"""
import time

import pyautogui


def move():
    """This function moves the mouse and clicks"""
    print(" ------ Execution -----\n")
    pyautogui.moveRel(0, 10)
    pyautogui.moveRel(0, -10)
    pyautogui.click()


while True:
    time.sleep(15 * 60)  # Call the move function after every 15 mins
    move()
