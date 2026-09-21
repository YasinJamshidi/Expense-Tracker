import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    title = input("Expense title: ")

    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Please enter a valid amount.")
        return

    expense = {
        "title": title,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully.")


def show_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    total = 0

    print("\n--- Expenses ---")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['title']} - ${expense['amount']:.2f}")
        total += expense["amount"]

    print(f"\nTotal: ${total:.2f}")


def delete_expense(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n--- Select an expense to delete ---")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['title']} - ${expense['amount']:.2f}")

    try:
        choice = int(input("\nSelect number: "))

        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)
            save_expenses(expenses)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid number.")

    except ValueError:
        print("Please enter a number.")


def main():
    expenses = load_expenses()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Delete expense")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            delete_expense(expenses)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
