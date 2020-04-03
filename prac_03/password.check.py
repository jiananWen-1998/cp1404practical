"""Get a password with minimum length and display asterisks"""

"""https://github.com/jiananWen-1998/cp1404practical"""

min_length = 4
def main():
    """Get and print password """
    password = get_password(min_length)
    print_asterisks(password)
def get_password(min_length):
    """Get password, ensuring it meets the min_length requirement."""
    password = input("Enter the password at least {} characters:".format(min_length))
    while len(password) < min_length:
        print("Password is too short,Please try again")
        password = input("Enter the password at least {} characters:".format(min_length))
    return password

def print_asterisks(password):
    """Print as many asterisks as there are characters in the passed-in sequence."""
    print("*"* len(password))
if __name__ == '__main__':
    main()