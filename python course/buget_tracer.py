# Simple Text-Based Budget Tracker in Python

# Initialize an empty dictionary to store expenses
expenses = {}

def add_expense():
    """Add an expense to the tracker."""
    category = input("Enter the expense category: ")
    amount = float(input("Enter the expense amount: $"))
    
    # Add the expense to the dictionary
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount
    
    print(f"Added ${amount:.2f} to category '{category}'.")

def view_expenses():
    """View the expenses summary."""
    print("\nExpense Summary:")
    if not expenses:
        print("No expenses recorded.")
        return
    
    total = 0
    for category, amount in expenses.items():
        print(f"Category: {category}, Amount: ${amount:.2f}")
        total += amount
    
    print(f"\nTotal Expenses: ${total:.2f}")

def main():
    """Main function to run the budget tracker."""
    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Exiting the budget tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
########################################################################################################
# Simple Text-Based Budget Tracker

# Initialize an empty list to store expenses
expenses = []

def add_expense():
    """Prompt the user to add an expense."""
    category = input("Enter the expense category (e.g., food, transport, entertainment): ")
    amount = float(input("Enter the expense amount: $"))
    expenses.append((category, amount))
    print(f"Added ${amount:.2f} to category '{category}'.")

def view_expenses():
    """Print all expenses in the list."""
    if not expenses:
        print("No expenses recorded.")
        return
    
    print("\nExpense List:")
    total = 0
    for category, amount in expenses:
        print(f"Category: {category}, Amount: ${amount:.2f}")
        total += amount
    print(f"\nTotal Expenses: ${total:.2f}")

def main():
    """Main loop to interact with the user."""
    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Exiting the budget tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
#######
#Steps Explained:
#Introduction: The program lets users add and view categorized expenses.
#Create a List: Expenses are stored in a list as tuples, each with a category and amount.
#Add Expenses: Prompts the user for a category and amount, then adds the expense to the list.
#View Expenses: Loops through the list and prints each expense with its category and amount.
#Main Loop: Continuously displays a menu for the user to add expenses, view them, or exit, and keeps the program running based on user input.
#You can save this code to a file, such as budget_tracker.py, and run it using Python.
########