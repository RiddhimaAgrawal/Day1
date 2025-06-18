
from functions import load_expenses, save_expenses

def print_expenses(expenses):
    '''to print the expenses'''
    print(f"{'Date':<12}{'Category':<15}{'Amount':<10}{'Description'}")
    print("-" * 50)
    for e in expenses:
        print(f"{e['date']:<12}{e['category']:<15}{e['amount']:<10}{e['description']}")

if __name__ == '__main__':
    expenses = load_expenses()

    # Example data (optional - you can skip this if file already exists)
    if not expenses:
        expenses = [
            {'date': '2025-06-18', 'category': 'Food', 'amount': '150', 'description': 'Lunch'},
            {'date': '2025-06-18', 'category': 'Transport', 'amount': '50', 'description': 'Bus fare'}
        ]
        save_expenses(expenses)

    print_expenses(expenses)
