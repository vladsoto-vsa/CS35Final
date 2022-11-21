"""
This program will keep track the amount of tips and customers
"""

def main():

    customers = int(input("Enter the number of customers: "))
    total = 0
    for i in range(customers):
        print("Customer", i+1)
        amount = float(input("Enter the amount spent: "))
        print("tip: $"+str(amount * .100))
        total = total + (amount * .100)

    print("Total tip amount: $" + str(total))

main()
