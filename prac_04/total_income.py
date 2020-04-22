"""
CP1404/CP5632 Practical - Suggested Solution
Cumulative total income program
"""

def main():
    incomes = []
    number_of_months = int(input("How many months:"))
    for month in range(1,number_of_months + 1):
        income = float(input("Enter income for month{}:".format(month)))
        incomes.append(income)
    print_report(incomes)

def print_report(incomes):
    """Print report based on incomes"""
    print("\nIncomes report\n")
    total = 0
    for month, incomes in enumerate(incomes):
        total = total + incomes
        print("Month {:2} - Income: ${:10.2f} \ntotal: ${:10.2f}".format(month + 1, incomes, total))

if __name__ == '__main__':
    main()