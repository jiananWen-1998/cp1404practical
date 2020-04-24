"""
CP1404/CP5632 Practical - Suggested Solution
Email to name dictionary
"""

def main():
    """Create dictionary of emails-to-names."""
    email_to_name = {}
    email = input("Email:")
    while email != "" :
        name = get_name_from_email(email)
        confirmation = input("Is your name{}?(Y/n)".format(name))
        if confirmation.upper()!= "Y" and confirmation !="":
            name = input("Names:")
        email_to_name[email] = name
        email = input("Email:")


    for email,name in email_to_name.item():
        print("{} ({})".format(name, email))

def get_name_from_email(email):
    """Extract expected name from email address."""
    perfix = email.split('@')[0]
    parts = perfix.split('.')
    name = "".join(parts).title()
    return name

if __name__ == '__main__':
    main()
