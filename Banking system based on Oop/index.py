class BankAccount:
    # Constructor to initialize the account
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Withdraw amount must be positive.")

    # Method to display account information
    def display_account(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance}")

# Main program
if __name__ == "__main__":
    # Create an account
    account = BankAccount("Hassan", 1000)
    # Display account information
    account.display_account()
    # Deposit money
    account.deposit(500)
    # Withdraw money
    account.withdraw(300)
    # Display account information again
    account.display_account()
