"""Quick file opening / writing / reading exercises
"""
# Quick Program 1
def main():
    out_file = open("name.txt","w")
    name = input("What is your name? ")
    out_file.write(name)
    out_file.close()
# Quick Program 2
    in_file = open("name.txt","r")
    print("Your name is", name)
    in_file.close()
# Quick Program 3
    in_file = open("numbers.txt","r")
    num1 = int(in_file.readline())
    num2 = int(in_file.readline())
    in_file.close()
    print(num1 + num2)
# Quick Program 4
    in_file = open("numbers.txt","r")
    for numbers in in_file:
        total = 0
        number = int(numbers)
        total = total + number
        print(total)
    in_file.close()
if __name__ == '__main__':
    main()