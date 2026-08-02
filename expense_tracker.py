expenses = []

def AddExpense():
    print("ADDING THE EXPENSE...")

    name = input("Name: ")
    category = input("Category: ")
    amount = float(input("Amount: "))

    expense = {
        "name": name,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    print("Expense added successfully")
    print(name)
    print(amount)
    print(category)

def ViewExpense():
    for expense in expenses:
        print("View your Expenses")
        print("Name:", expense["name"])
        print("Category:", expense["category"])
        print("Amount:", expense["amount"])

def SearchExpense():
    print("Searching for your expense according to category")

    if len(expenses) == 0:
        print("No expenses available.")
        return
  
    search = input("Type the category you want to searcch: ")

    found = False

    for expense in expenses:
        if expense["category"].lower() == search.lower():
            print("Expense you search...")
            print("Name     :", expense["name"])
            print("Category :", expense["category"])
            print("Amount   :", expense["amount"])

            found = True

    if found == False:
        print("No expense found.")
    
def TotalExpense():
    print("Total expense is here")

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total Expense =", total)

def HighestExpense():

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


while True:
    print("MENU")
    print("1..ADD EXPENSE")
    print("2..SEARCH EXPENSE")
    print("3..VIEW EXPENSE")
    print("4..TOTAL EXPENSE")
    print("5..Highest Expense")
    print("6..EXIT")

    choice = input("Enter your choice: ")

    print(choice)

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
        print("Invalid choice")





  