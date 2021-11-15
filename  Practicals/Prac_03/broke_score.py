"""
CP1404/CP5632 - Practical
Roderick Mabo Broken Program status
"""

import random


def main(score):
    if score < 0:
        print("Invaild Score")
    elif score > 100:
        print("Invaild Score")
    elif score > 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        return "BAD"


main()
