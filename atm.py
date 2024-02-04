class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

    def display_balance(self):
        return f"Your balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: ${amount}")
            return f"Withdrawal successful. {self.display_balance()}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: ${amount}")
            return f"Deposit successful. {self.display_balance()}"
        else:
            return "Invalid deposit amount."

    def transfer(self, recipient, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transfer to {recipient.user_id}: ${amount}")
            return f"Transfer successful. {self.display_balance()}"
        else:
            return "Invalid transfer amount or insufficient funds."


class ATM:
    def __init__(self):
        self.users = {}

    def start(self):
        user_id = input("Enter your user ID: ")
        pin = input("Enter your PIN: ")

        if user_id in self.users and self.users[user_id].pin == pin:
            return self.users[user_id]
        else:
            return None

    def display_menu(self):
        print("\nATM Menu:")
        print("1. Transactions History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Quit")

    def perform_transaction(self, user):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                print("\nTransaction History:")
                for transaction in user.transaction_history:
                    print(transaction)
            elif choice == "2":
                amount = float(input("Enter withdrawal amount: "))
                print(user.withdraw(amount))
            elif choice == "3":
                amount = float(input("Enter deposit amount: "))
                print(user.deposit(amount))
            elif choice == "4":
                recipient_id = input("Enter recipient's user ID: ")
                if recipient_id in self.users:
                    recipient = self.users[recipient_id]
                    amount = float(input("Enter transfer amount: "))
                    print(user.transfer(recipient, amount))
                else:
                    print("Recipient not found.")
            elif choice == "5":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


# Sample usage
atm = ATM()

# Create user accounts
atm.users["user123"] = User("user123", "1234")
atm.users["user456"] = User("user456", "5678")

# Start ATM session
user = atm.start()

if user:
    atm.perform_transaction(user)
else:
    print("Authentication failed. Invalid user ID or PIN.")
