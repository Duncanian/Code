#! python3
"""Saves a screenshot of a trade"""
import sys
import time
import datetime

from PIL import ImageGrab
import winsound


def screenshot(filename):
    time.sleep(10)
    snapshot = ImageGrab.grab()
    save_path = f"C:\\Users\\Admin\\Desktop\\FX\\{filename}-{datetime.date.today().strftime('%b-%d')}.jpg"  # noqa E501
    snapshot.save(save_path)
    winsound.Beep(1000, 160)


if __name__ == "__main__":
    filename = sys.argv[1]  # CURRENCY e.g. EUR-USD
    screenshot(filename)
