class BankAccount:
    """BankAccount class with deposit, withdraw, and balance display methods."""
    
    def __init__(self, account_number, account_holder, initial_balance=0.0):
        """Initialize account with account number, holder name, and balance."""
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        """Deposit money into account. Returns True if successful."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. Balance: ${self.balance:.2f}")
            return True
        else:
            print("Error: Deposit amount must be positive.")
            return False
    
    def withdraw(self, amount):
        """Withdraw money from account. Returns True if successful."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. Balance: ${self.balance:.2f}")
                return True
            else:
                print(f"Error: Insufficient funds. Balance: ${self.balance:.2f}")
                return False
        else:
            print("Error: Withdrawal amount must be positive.")
            return False
    
    def display_balance(self):
        """Display account holder, number, and current balance."""
        print(f"Account: {self.account_number}")
        print(f"Holder: {self.account_holder}")
        print(f"Balance: ${self.balance:.2f}")
        return self.balance


# Main program
if __name__ == "__main__":
    print("=" * 50)
    print("BANK ACCOUNT MANAGEMENT")
    print("=" * 50)
    
    # Create account
    account = BankAccount("ACC001", "John Doe", 1000.00)
    
    # Test methods
    account.deposit(500.00)
    account.withdraw(200.00)
    account.display_balance()
    
    print("\n" + "=" * 50)
    print("CODE ANALYSIS")
    print("=" * 50)
    print("""
    1. CLASS STRUCTURE:
       - BankAccount class with __init__, deposit, withdraw, display_balance
       - Attributes: account_number, account_holder, balance
    
    2. METHODS:
       - __init__: Initializes account with number, holder, balance
       - deposit: Adds money (validates positive amount)
       - withdraw: Removes money (validates positive and sufficient funds)
       - display_balance: Shows account information
    
    3. CODE QUALITY:
       ✓ Input validation for deposits/withdrawals
       ✓ Error handling with clear messages
       ✓ Encapsulation (data protected in class)
       ✓ All methods: O(1) time complexity
    
    4. BEST PRACTICES:
       ✓ Clear method names
       ✓ Proper error messages
       ✓ Balance validation before withdrawal
       ✓ Returns boolean for success/failure
    """)
