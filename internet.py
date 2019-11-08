#! python3
"""Schedules periodic internet connection tests"""
import time
from datetime import datetime
import webbrowser


def internet_test():
    """This function opens fast.com to check the internet connection"""
    print(f" ------ Execution  at {datetime.now().time()} -----\n")
    url = "https://fast.com/"
    webbrowser.open(url)


while True:
    time.sleep(30 * 60)  # Call the internet_test function after every 30 mins
    internet_test()
