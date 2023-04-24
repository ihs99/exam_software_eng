class ATM:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("You withdrew", amount, "dollars. Available balance:", self.balance)

    def deposit_cash(self, amount):
        # Actualizar el saldo
        self.balance += amount
        print("You deposited", amount, "dollars. Available balance:", self.balance)

    def deposit_check(self, amount):
        self.balance += amount
        print("You deposited a check for", amount, "dollars. Available balance:", self.balance)

class Customer:
    def __init__(self, bank_account):
        # Asociar la cuenta bancaria del cliente con el objetoo ATM
        self.bank_account = bank_account

    def check_balance(self):
        print("Your balance is", self.bank_account.balance, "dollars.")

    def withdraw(self, amount):
        self.bank_account.withdraw(amount)

    def deposit_cash(self, amount):
        self.bank_account.deposit_cash(amount)

    def deposit_check(self, amount):
        self.bank_account.deposit_check(amount)

class BankAccount:
    def __init__(self):
        self.balance = 0

    def update_balance(self, amount):
        self.balance += amount
        print("Your updated balance is", self.balance, "dollars.")