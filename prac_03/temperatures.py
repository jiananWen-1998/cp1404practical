"""Temperature conversionsTemperature conversions"""
# Note: this is a constant, so it is global, defined before main
"""https://github.com/jiananWen-1998/cp1404practical"""

list = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32
def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    return 5 / 9 * (fahrenheit - 32)

def main():
    print(list)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Enter the celsius:"))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print("Result:{:.2f}F" .format(fahrenheit))
        elif choice =="F":
            fahrenheit = float(input("Enter the fahrenhrit:"))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print("Result:{:.2f}C" .format(celsius))
        else:
            print("Invalid option")
        print(list)
        choice = input(">>>").upper()
    print("thank you")

if __name__ == '__main__':
    main()
