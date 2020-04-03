"""Fixed program to determine score status, with function"""

""" Author:jianan Wen
    Date : 04/03/2020
    link: https://github.com/jiananWen-1998/cp1404practical
"""
# Note boundary conditions (50 should be a pass, not > 50)
# Note efficiency and nesting; use the fewest number of if/elif as possible


def main():
    """Get score and display"""
    score = float(input("Enter your score:"))
    print(get_score(score))

def get_score(score):
    """Determine the status of a given score."""
    if  score< 0 or score >100:
        return "Incalid score"
    elif score>= 90:
        return "Excellent"
    elif score >=50:
        return "Pass"
    else:
        return"bad"
if __name__ == '__main__':
    main()