"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this
def main():
    """ main() method, starting point of program"""
    score = float(input("Enter your score:"))
    if score < 0 or score > 100 :
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("pass")
    else:
        print("Bad")
main()


