#! python3
"""Calculates position size and risk reward ratio"""
import sys


def calculate(loss, profit):
    risk_reward = round(profit / loss, 2)
    max_risk = 95  # Ksh 9,500
    volume = round(max_risk / (loss * 10), 2)
    print(f"---- \nR/R ratio: {risk_reward} | Max win: {max_risk * risk_reward} | Volume: {volume} \n----")  # noqa E501


if __name__ == "__main__":
    loss, profit = int(sys.argv[1]), int(sys.argv[2])  # python lot.py 50 100
    calculate(loss, profit)
