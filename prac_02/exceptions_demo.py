"""Answer the question
1.When will a ValueError occur?
2.When will a ZeroDivisionError occur?"""
"""3.Could you change the code to avoid the possibility of a ZeroDivisionError?"""
def main():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        while denominator == 0:
            print("Error: denomirator cannnot be 0 ")
            denominator = int(input("Enter the denominator:"))
        else:
            fraction = numerator / denominator
            print(fraction)
        print("Finished")
    except ValueError:
        print("Numerator and denominator be valid numbers")
if __name__ == '__main__':
    main()


