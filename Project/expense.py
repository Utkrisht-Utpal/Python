expenses = {}

while True:
    print("💵 Welcome to expenses Tracker 💵")

    print("--- Tracker Menu ---")
    print("1. Add expenses")
    print("2. View expenses")
    print("3. View Total expenses")
    print("4. Exit")
    choice = int(input("Choose an operation: (1 - 4): "))

    if choice == 1:
        date = input("Enter the date you want to log into: ")
        category = input("Enter the category of expense: ")
        amount = float(input("Enter the amount: "))

        if date in expenses:
            expenses[date].append({"category ": category, " | amount":amount})
        else:
            expenses [date] = [{"category ": category, " | amount":amount}]
    
    elif choice == 2:
        if expenses:
            for date in expenses:
                print("Date: ", date)
                for item in expenses[date]:
                    print("Categroy: ", item[category], "Amount: ", item[amount])
        else: print("No expenses found!")
    
    elif choice == 3:
        total = 0
        for date in expenses:
            for item in expenses[date]:
                total += item["amount"]

        print("Total expenses =", total)

    elif choice == 4:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice, try again!")