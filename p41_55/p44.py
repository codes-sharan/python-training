# Simple Bank Software

class BankAccount:
    def __init__(self, name, phone, balance=0.00):
        self.name = name
        self.phone = phone
        self.balance = balance

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"Successfull deposit ${amount:.2f} to {self.name} account")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawan ${amount:.2f} from {self.name}'s account")
        else:
            print("Invalid withdraw amount or insufficient amount")

    def get_amount(self):
        return f"{self.name}'s current balance: ${self.balance}"


# ram = BankAccount("Hari Sharma", '9856456')
# ram.deposit(5000)
# ram.withdraw(2000)

# print(ram.get_amount())



gopal = BankAccount("Hari Sharma", '9856456')
gopal.deposit(0)
gopal.withdraw(2000)

print(gopal.get_amount())