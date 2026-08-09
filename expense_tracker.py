from mysql_db import MySQLDB


def add_expense(db):
    print("\nADDING THE EXPENSE")
    print("------------------")

    try:
        name = input("Name: ").strip()
        category = input("Category: ").strip()
        amount = float(input("Amount: "))

        if not name:
            print("Name cannot be empty.")
            return

        if not category:
            print("Category cannot be empty.")
            return

        if amount < 0:
            print("Amount cannot be negative.")
            return

        db.add_expense(name, category, amount)

    except ValueError:
        print("Please enter a valid amount.")


def view_expenses(db):
    print("\nYOUR EXPENSES")
    print("-------------")

    rows = db.view_expenses()

    if not rows:
        print("No expenses available.")
        return

    for row in rows:
        print("----------------")
        print("ID:", row[0])
        print("Name:", row[1])
        print("Category:", row[2])
        print("Amount:", row[3])


def search_expenses(db):
    print("\nSEARCH EXPENSE")
    print("--------------")

    category = input("Enter category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    rows = db.search_expenses(category)

    if not rows:
        print("No expenses found.")
        return

    for row in rows:
        print("----------------")
        print("ID:", row[0])
        print("Name:", row[1])
        print("Category:", row[2])
        print("Amount:", row[3])


def update_expense(db):
    print("\nUPDATE EXPENSE")
    print("--------------")

    try:
        expense_id = int(input("Enter expense ID: "))

        name = input("New name: ").strip()
        category = input("New category: ").strip()
        amount = float(input("New amount: "))

        if not name:
            print("Name cannot be empty.")
            return

        if not category:
            print("Category cannot be empty.")
            return

        if amount < 0:
            print("Amount cannot be negative.")
            return

        result = db.update_expense(
            expense_id,
            name,
            category,
            amount
        )

        if result > 0:
            print("Expense updated successfully!")
        else:
            print("Expense not found.")

    except ValueError:
        print("Please enter valid values.")


def delete_expense(db):
    print("\nDELETE EXPENSE")
    print("--------------")

    try:
        expense_id = int(input("Enter expense ID: "))

        result = db.delete_expense(expense_id)

        if result > 0:
            print("Expense deleted successfully!")
        else:
            print("Expense not found.")

    except ValueError:
        print("Please enter a valid ID.")


def total_expense(db):
    print("\nTOTAL EXPENSE")
    print("-------------")

    total = db.total_expense()

    print("Total Expense:", total)


def highest_expense(db):
    print("\nHIGHEST EXPENSE")
    print("---------------")

    highest = db.highest_expense()

    if highest:
        print("ID:", highest[0])
        print("Name:", highest[1])
        print("Category:", highest[2])
        print("Amount:", highest[3])
    else:
        print("No expenses found.")


def main():

    try:
        db = MySQLDB()

        while True:

            print("\n======================")
            print("     EXPENSE TRACKER")
            print("======================")

            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Search Expense")
            print("4. Update Expense")
            print("5. Delete Expense")
            print("6. Total Expense")
            print("7. Highest Expense")
            print("8. Exit")

            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                add_expense(db)

            elif choice == "2":
                view_expenses(db)

            elif choice == "3":
                search_expenses(db)

            elif choice == "4":
                update_expense(db)

            elif choice == "5":
                delete_expense(db)

            elif choice == "6":
                total_expense(db)

            elif choice == "7":
                highest_expense(db)

            elif choice == "8":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please choose 1-8.")

        db.close()

    except Exception as e:
        print("An unexpected error occurred:", e)


if __name__ == "__main__":
    main()