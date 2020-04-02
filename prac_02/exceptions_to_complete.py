"""Fill in the TODOs to complete the task
"""
def main():
    finished = False
    result = 0
    while not finished:
        try:
            result = int(input("Enter an integer:"))
            finished = True

        except ValueError:
            print("Please enter a valid integer.")
    print("Valid result is:", result)

if __name__ == '__main__':
    main()