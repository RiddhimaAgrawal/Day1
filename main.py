from functions import (
    ExpenseManager,
    CreateExpense,
    ListExpenses,
    UpdateExpense,
    DeleteExpense,
    SearchExpense
)

def main():
    manager = ExpenseManager()

    while True:
        print("\n==== Expense Tracker Menu ====")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Search Expenses")
        print("6. Filter by Category")
        print("7. Filter by Date Range")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            description = input("Enter description: ")
            CreateExpense(manager).run(date, category, amount, description)

        elif choice == '2':
            ListExpenses(manager).run()

        elif choice == '3':
            ListExpenses(manager).run()
            try:
                index = int(input("Enter index of expense to update: "))
                field = input("Enter field to update (date, category, amount, description): ")
                new_value = input("Enter new value: ")
                UpdateExpense(manager).run(index, field, new_value)
            except ValueError:
                print("❌ Invalid input.")

        elif choice == '4':
            ListExpenses(manager).run()
            try:
                index = int(input("Enter index of expense to delete: "))
                DeleteExpense(manager).run(index)
            except ValueError:
                print("❌ Invalid input.")

        elif choice == '5':
            keyword = input("Enter keyword to search: ")
            SearchExpense(manager).run(keyword)

       elif choice == '6':
            cat = input("Enter category to filter: ")
            manager.filter_by_category(cat)

        elif choice == '7':
            start = input("Enter start date (YYYY-MM-DD): ")
            end = input("Enter end date (YYYY-MM-DD): ")
            manager.filter_by_date_range(start, end)

        elif choice == '8':
            print(" Exiting. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()
