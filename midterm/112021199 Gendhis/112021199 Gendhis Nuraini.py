from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime

@dataclass
class Transaction:
    amount: float
    timestamp: datetime

@dataclass
class Expense(Transaction):
    category: str

@dataclass
class MoneyData:
    income: List[Transaction]
    expenses: Dict[str, List[Expense]]
    max_expense: float

    def __init__(self, max_expense: float):
        self.income = []
        self.expenses = {}
        self.max_expense = max_expense

    def add_income(self, income_amount: float) -> None:
        timestamp = datetime.now()
        self.income.append(Transaction(income_amount, timestamp))

    def remove_income(self, index: int) -> None:
        if 0 <= index < len(self.income):
            del self.income[index]

    def edit_income(self, index: int, new_income: float) -> None:
        if 0 <= index < len(self.income):
            self.income[index].amount = new_income

    def view_income(self) -> None:
        print("Income:")
        for i, transaction in enumerate(self.income, start=1):
            timestamp_str = transaction.timestamp.strftime("%Y-%m-%d %H:%M")
            print(f"{i}: Amount: {transaction.amount}, Transaction Date: {timestamp_str}")

    def calculate_avg_revenue(self) -> float:
        if not self.income:
            return 0
        return sum(transaction.amount for transaction in self.income) / len(self.income)

    def calculate_total_income(self) -> float:
        return sum(transaction.amount for transaction in self.income)

    def add_expense(self, expense_amount: float, category: str) -> None:
        if expense_amount > self.max_expense:
            print("Expenses exceed maximum limit!")
        else:
            timestamp = datetime.now()
            expense = Expense(expense_amount, timestamp, category)
            if category in self.expenses:
                self.expenses[category].append(expense)
            else:
                self.expenses[category] = [expense]

    def remove_expense(self, category: str, index: int) -> None:
        if category in self.expenses and 0 <= index < len(self.expenses[category]):
            del self.expenses[category][index]

    def view_expenses(self) -> None:
        print("Expenses:")
        for category, transactions in self.expenses.items():
            print(f"{category}:")
            for i, transaction in enumerate(transactions, start=1):
                timestamp_str = transaction.timestamp.strftime("%Y-%m-%d %H:%M")
                print(f"  {i}: Amount: {transaction.amount}, Category: {transaction.category}, Transaction Date: {timestamp_str}")

    def calculate_avg_expenditures(self) -> Dict[str, float]:
        avg_expenditures = {}
        for category, transactions in self.expenses.items():
            if transactions:
                avg_expenditures[category] = sum(transaction.amount for transaction in transactions) / len(transactions)
            else:
                avg_expenditures[category] = 0
        return avg_expenditures

    def calculate_total_expense(self) -> float:
        return sum(sum(transaction.amount for transaction in transactions) for transactions in self.expenses.values())

    def calculate_total_money(self) -> float:
        total_income = self.calculate_total_income()
        total_expense = self.calculate_total_expense()
        return total_income - total_expense


class Money:
    def __init__(self):
        max_expense = float(input("Enter the maximum spending limit per month: "))
        self.data = MoneyData(max_expense)

    def handle_menu_choice(self, choice: str) -> None:
        if choice == "1":
            income_amount = float(input("Enter income amount: "))
            self.data.add_income(income_amount)
        elif choice == "2":
            index = int(input("Enter index of income to remove: "))
            self.data.remove_income(index - 1)
        elif choice == "3":
            index = int(input("Enter index of income to edit: "))
            new_income = float(input("Enter new income amount: "))
            self.data.edit_income(index - 1, new_income)
        elif choice == "4":
            self.data.view_income()
        elif choice == "5":
            avg_revenue = self.data.calculate_avg_revenue()
            print(f"Average monthly incomes: {avg_revenue}")
        elif choice == "6":
            total_income = self.data.calculate_total_income()
            print(f"Total income: {total_income}")
        elif choice == "7":
            expense_amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            self.data.add_expense(expense_amount, category)
        elif choice == "8":
            category = input("Enter expense category: ")
            index = int(input("Enter index of expense to remove: "))
            self.data.remove_expense(category, index - 1)
        elif choice == "9":
            category = input("Enter expense category: ")
            index = int(input("Enter index of expense to edit: "))
            new_amount = float(input("Enter new expense amount: "))
            self.data.expenses[category][index - 1].amount = new_amount
        elif choice == "10":
            self.data.view_expenses()
        elif choice == "11":
            avg_expenditures = self.data.calculate_avg_expenditures()
            print("Average monthly expenditures:")
            for category, avg_expenditure in avg_expenditures.items():
                print(f"{category}: {avg_expenditure}")
        elif choice == "12":
            total_expense = self.data.calculate_total_expense()
            print(f"Total expense: {total_expense}")
        elif choice == "13":
            total_money = self.data.calculate_total_money()
            print(f"Total money: {total_money}")
        elif choice == "14":
            print("Program finished.")
        else:
            print("Invalid choice.")

    def run(self) -> None:
        while True:
            print("\nMenu:")
            print("1. Add Income")
            print("2. Remove Income")
            print("3. Edit Income")
            print("4. View Income")
            print("5. Calculate Average Revenue")
            print("6. Calculate Total Income")
            print("7. Add Expense")
            print("8. Remove Expense")
            print("9. Edit Expense")
            print("10. View Expenses")
            print("11. Calculate Average Expenditures")
            print("12. Calculate Total Expense")
            print("13. Calculate Total Money")
            print("14. Finish")

            choice = input("Choose: ")

            if choice == "14":
                break

            self.handle_menu_choice(choice)


if __name__ == "__main__":
    money = Money()
    money.run()
