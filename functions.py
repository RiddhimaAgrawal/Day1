import csv

class ExpenseManager:
    def __init__(self, filename='expenses.csv'):
        self.filename = filename
        self.headers = ['date', 'category', 'amount', 'description']
        self.expenses = self.load_expenses()

    def load_expenses(self):
        expenses = []
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    expenses.append(row)
        except FileNotFoundError:
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.headers)
                writer.writeheader()
        return expenses

    def save_expenses(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            writer.writeheader()
            for expense in self.expenses:
                writer.writerow(expense)
class CreateExpense:
    def __init__(self, manager: ExpenseManager):
        self.manager = manager

    def run(self, date, category, amount, description):
        new_expense = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        }
        self.manager.expenses.append(new_expense)
        self.manager.save_expenses()
        print("✅ Expense created.")
from tabulate import tabulate

class ListExpenses:
    def __init__(self, manager: ExpenseManager):
        self.manager = manager

    def run(self):
        if not self.manager.expenses:
            print("No expenses recorded.")
        else:
            print(tabulate(self.manager.expenses, headers="keys", showindex=True, tablefmt="grid"))
class UpdateExpense:
    def __init__(self, manager: ExpenseManager):
        self.manager = manager

    def run(self, index, field, new_value):
        try:
            self.manager.expenses[index][field] = new_value
            self.manager.save_expenses()
            print("✅ Expense updated.")
        except (IndexError, KeyError):
            print("❌ Invalid index or field.")
class DeleteExpense:
    def __init__(self, manager: ExpenseManager):
        self.manager = manager

    def run(self, index):
        try:
            removed = self.manager.expenses.pop(index)
            self.manager.save_expenses()
            print(f"🗑 Deleted: {removed}")
        except IndexError:
            print("❌ Invalid index.")
class SearchExpense:
    def __init__(self, manager: ExpenseManager):
        self.manager = manager

    def run(self, keyword):
        keyword = keyword.lower()
        results = [
            e for e in self.manager.expenses
            if keyword in e['category'].lower() or keyword in e['description'].lower()
        ]
        if results:
            print(tabulate(results, headers="keys", tablefmt="grid"))
        else:
            print("🔍 No matching expenses.")
