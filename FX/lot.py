#! python3
"""Calculates appropriate position size"""
import sys
import locale
locale.setlocale(locale.LC_ALL, '')


def calculate(balance, breather=25, percentage=5):
    perc = percentage / 100
    pip_val = breather * 11
    risk_capital = perc * balance
    volume = round(risk_capital / pip_val, 2)

    print(f"----- \nVOLUME: {volume} | RISK CAPITAL: Ksh.{round(risk_capital * 100, 2):n} of | Ksh.{round(balance * 100, 2):n}\n-----")  # noqa E501


if __name__ == "__main__":
    balance = float(sys.argv[1])  # python lot.py 600 30 3

    if len(sys.argv) == 3:
        breather = float(sys.argv[2])
        calculate(balance, breather=breather)
    elif len(sys.argv) == 4:
        breather = float(sys.argv[2])
        percentage = float(sys.argv[3])
        calculate(balance, breather=breather, percentage=percentage)
    else:
        calculate(balance)
