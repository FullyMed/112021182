from dataclasses import dataclass
import pprint
from datetime import datetime
import csv
import os

@dataclass
class Expense:
    date: datetime
    category: str
    amount: float

def create_csv_if_not_exists():
    csv_file_name = 'expenses.csv'
    if not os.path.isfile(csv_file_name):
        with open(csv_file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Date", "Category", "Amount"])

def upload_expense():
    expenses = []
    csv_file_name = 'expenses.csv'
    if os.path.isfile(csv_file_name):
        with open(csv_file_name, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader) 
            for row in reader:
                date = datetime.strptime(row[0], "%Y-%m-%d")
                category = row[1]
                amount = float(row[2])
                expenses.append(Expense(date, category, amount))
    return expenses

def save_expenses(expenses):
    csv_file_name = 'expenses.csv'
    with open(csv_file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Date", "Category", "Amount"])  
        for expense in expenses:
            writer.writerow([expense.date.strftime("%Y-%m-%d"), expense.category, expense.amount])

print("Finance Tracker")
menu = ["1. Add expense", "2. Edit expense", "3. Remove expense", "4. Print out expenses"]
pprint.pprint(menu)
create_csv_if_not_exists()
expenses = upload_expense()

while True:
    print("Please select a function")
    function = input()
    match function:
        case "1":
            print("Add expense")
            date = datetime.strptime(input('Please enter date (yy-mm-dd): '), "%y-%m-%d")
            print("Date: ", date)
            category = input("Category: ")
            amount = float(input("Amount: "))
            new_expense = Expense(date, category, amount)
            expenses.append(new_expense)
            save_expenses(expenses)
        case "2":
            print("Edit expense")
            print("Please choose transaction to edit")
            for i, expense in enumerate(expenses):
                print(f"{i+1}. Date: {expense.date}, Category: {expense.category}, Amount: {expense.amount}")
            index = int(input("Enter the index of the expense you want to edit: ")) - 1
            if 0 <= index < len(expenses):
                new_category = input("Enter new category: ")
                new_amount = float(input("Enter new amount: "))
                expenses[index] = Expense(expenses[index].date, new_category, new_amount)
                save_expenses(expenses)
                print("Expense edited successfully!")
            else: 
                print("Invalid index")
        case "3":
            print("Remove expense")
            for i, expense in enumerate(expenses):
                print(f"{i+1}. Date: {expense.date}, Category: {expense.category}, Amount: {expense.amount}")
            index = int(input("Enter the number of the expense you want to delete: ")) - 1
            if 0 <= index < len(expenses):
                del expenses[index]
                save_expenses(expenses)
                print("Expense deleted successfully!")
            else:
                print("Invalid index")
        case "4":
            print("Print expenses")
            with open('expenses.csv', 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    print(*row, sep=',')
        case _:
              print("Thank you for using the app today!")
    
     
    
    

