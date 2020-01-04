#! python3
"""Calcultes trading statistics"""
import os


def main():
    """Calcultes trading statisticsfor all trades"""
    wins = len(os.listdir("C:\\Users\\Admin\\Desktop\\FX\\WINS")) - 1  # noqa E501
    losses = len(os.listdir("C:\\Users\\Admin\\Desktop\\FX\\LOSSES")) - 1  # noqa E501
    total = wins + losses
    win_ratio = round((wins / total) * 100, 2)
    print(f"{wins} wins, {losses} losses, your win ratio is {win_ratio} per cent")  # noqa E501


def majors():
    """Calcultes trading statistics for the majors"""
    wpath = "C:\\Users\\Admin\\Desktop\\FX\\WINS"
    lpath = "C:\\Users\\Admin\\Desktop\\FX\\LOSSES"
    wins, losses = (0, 0)

    for win in os.listdir(wpath):
        if "USD" in win:
            wins += 1

    for loss in os.listdir(lpath):
        if "USD" in loss:
            losses += 1

    total = wins + losses
    win_ratio = round((wins / total) * 100, 2)
    print(f"\nMajors: {wins} wins, {losses} losses, your win ratio is {win_ratio} per cent\n")  # noqa E501


if __name__ == "__main__":
    main()
    majors()
