import csv

CSV_FILE = 'expenses.csv'
HEADERS = ['date', 'category', 'amount', 'description']

def load_expenses():
    '''read expense records and convert too python'''
    expenses = []
    try:
        with open(CSV_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    except FileNotFoundError:
        # Create the file if not found
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=HEADERS)
            writer.writeheader()
    return expenses

def save_expenses(expenses):
    '''write a list of expenses to csv'''
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        writer.writeheader()
        for expense in expenses:
            if set(expense.keys()) != set(HEADERS):
                print("❌ Mismatched keys in:", expense)
                continue
            writer.writerow(expense)
