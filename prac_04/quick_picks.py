""""Quick Pick" Lottery Ticket Generator"""

import random

number_each_line = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    number_of_quick_numbers = int(input("How many quick picks:"))
    while number_of_quick_numbers < 0 :
        print("Please try again:")
        number_of_quick_numbers = int(input("How many quick picks:"))

    for i in range(number_of_quick_numbers):
        quick_picks = []
        for m in range(number_each_line):
            number = random.randint(MIN_NUMBER,MAX_NUMBER)

            while number in quick_picks:
                number = random.randint(MIN_NUMBER,MAX_NUMBER)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join("{:2}".format(number) for number in quick_picks))
main()
