class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Not enough money")

    def get_balance(self):
        return self._balance


def main():
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(10)
    print(account.get_balance())

    account2 = BankAccount(200)
    account2.deposit(100)
    account2.withdraw(250)
    print(account2.get_balance())

if __name__ == "__main__":
    main()