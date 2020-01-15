#! python3
"""Calculates position size and risk reward ratio"""
import sys
import locale

locale.setlocale(locale.LC_ALL, '')


def calculate(loss, profit):
    risk_reward = round(profit / loss, 2)
    max_risk = 50  # Ksh 5,000
    raw_volume = max_risk / (loss * 10.0)
    volume = round(raw_volume, 2)
    print(f"---- \nR/R ratio: {risk_reward} | Max win: {(max_risk * risk_reward) * 100 :n} | Volume: {volume} ({raw_volume}) \n----")  # noqa E501


if __name__ == "__main__":
    loss, profit = int(sys.argv[1]), int(sys.argv[2])  # python lot.py 50 100
    calculate(loss, profit)
