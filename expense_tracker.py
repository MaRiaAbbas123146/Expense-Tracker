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
        print("----------------")
        print("Name:", expense["name"])
        print("Category:", expense["category"])
        print("Amount:", expense["amount"])

def SearchExpense():
    print("Searching for your expense according to category")
    search = input("Type the category you want to searcch: ")
    for expense in expenses:
        if expense["category"]==search:
            print("Expense you search...")

while True:
    print("MENU")
    print("1..ADD EXPENSE")
    print("2..SEARCH EXPENSE")
    print("3..VIEW EXPENSE")
    print("4..TOTAL EXPENSE")
    print("5..EXIT")

    choice = input("Enter your choice: ")

    print(choice)

    if choice == "1":
        AddExpense()

    elif choice == "2":
        ...

    elif choice == "3":
        ViewExpense()

    elif choice == "4":
        ...

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")





  