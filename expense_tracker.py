expenses = []


def AddExpense():
    try:
        print("ADDING THE EXPENSE...")

        name = input("Name: ").strip()
        category = input("Category: ").strip()

        if not name:
            raise ValueError("Name cannot be empty.")

        if not category:
            raise ValueError("Category cannot be empty.")

        amount = float(input("Amount: "))

        if amount < 0:
            raise ValueError("Amount cannot be negative.")

        expense = {
            "name": name,
            "category": category,
            "amount": amount
        }

        expenses.append(expense)

        print("Expense added successfully")
        print("Name:", name)
        print("Amount:", amount)
        print("Category:", category)

    except ValueError as e:
        print("Invalid input:", e)

    except Exception as e:
        print("An unexpected error occurred:", e)


def ViewExpense():
    try:
        print("\nVIEW YOUR EXPENSES")

        if len(expenses) == 0:
            print("No expenses available.")
            return

        for expense in expenses:
            print("----------------")
            print("Name:", expense["name"])
            print("Category:", expense["category"])
            print("Amount:", expense["amount"])

    except Exception as e:
        print("An unexpected error occurred:", e)


def SearchExpense():
    try:
        print("\nSEARCHING FOR YOUR EXPENSE ACCORDING TO CATEGORY")

        if len(expenses) == 0:
            print("No expenses available.")
            return

        search = input("Type the category you want to search: ").strip()

        if not search:
            raise ValueError("Search category cannot be empty.")

        found = False

        for expense in expenses:
            if expense["category"].lower() == search.lower():
                print("\nExpense found!")
                print("Name     :", expense["name"])
                print("Category :", expense["category"])
                print("Amount   :", expense["amount"])

                found = True

        if found == False:
            print("No expense found.")

    except ValueError as e:
        print("Invalid input:", e)

    except Exception as e:
        print("An unexpected error occurred:", e)


def TotalExpense():
    try:
        print("\nTOTAL EXPENSE")

        total = 0

        for expense in expenses:
            total += expense["amount"]

        print("Total Expense =", total)

    except Exception as e:
        print("An unexpected error occurred:", e)


def HighestExpense():
    try:
        if len(expenses) == 0:
            print("No expenses found.")
            return

        highest = expenses[0]

        for expense in expenses:
            if expense["amount"] > highest["amount"]:
                highest = expense

        print("\nHighest Expense")
        print("----------------")
        print("Name:", highest["name"])
        print("Category:", highest["category"])
        print("Amount:", highest["amount"])

    except Exception as e:
        print("An unexpected error occurred:", e)


while True:
    try:
        print("\nMENU")
        print("1.. ADD EXPENSE")
        print("2.. SEARCH EXPENSE")
        print("3.. VIEW EXPENSE")
        print("4.. TOTAL EXPENSE")
        print("5.. HIGHEST EXPENSE")
        print("6.. EXIT")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            AddExpense()

        elif choice == "2":
            SearchExpense()

        elif choice == "3":
            ViewExpense()

        elif choice == "4":
            TotalExpense()

        elif choice == "5":
            HighestExpense()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
        break

    except EOFError:
        print("\nInput was interrupted.")
        break

    except Exception as e:
        print("An unexpected error occurred:", e)