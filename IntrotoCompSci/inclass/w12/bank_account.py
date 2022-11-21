class BankAccount(object):
    def_init__(self,name, init_balance)
        self.name = name
        self.balance = init_balance
        self.acctnum = 1234
    def __str__(self):
        return "Account: %d Name: %s Balance: $%.2f" % \
            (self.acctnum, self.name, self.balance)
    def getBalance(self):
        return self.balance
    def getAcctNum(self):
        return self.acctnum
    def getName(self):
        return self.name
    def deposit(self, amount):
        if amount <= 0:
            print("Error: Invalid deposit amount %.2f" % (amount))
        else:
            self.balance = self.balance + amount
    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Invalid withdraw amount %.2f" % (amount))
        elif amount > self.balance:
            print("Error: Insufficient funds for withdraw amount %.2f" % \
                    (amount))

        else:
            self.balance = self.balance + amount



def main():
    acct = BankAccount("Vlad Soto", 100)
    print(acct)
    print("Current balance is: ", acct.getBalance())
    acc.deposit(50)
    print("After deposit, current balance is: ", acct.getBalance())
    acct.withdraw(100)
    print(acct)
    acct.withdraw(1000)
    print(acct)


main()
