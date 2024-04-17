class Money:
    def __init__(self):
        self.income = []
        self.outcome = []
        self.max_outcome = float(input("Enter the maximum spending limit per month : "))

    def add_income(self, income):
        self.income.append(float(income))
        print("Income Added Successfully")

    def remove_income(self, index):
        if 0 <= index < len(self.income):
            self.income.pop(index)
            print("Income Removed Successfully")
        else:
            print("Invalid index")

    def edit_income(self, index, new_income):
        if 0 <= index < len(self.income):
            self.income[index] = new_income
            print("Income Edited Successfully")
        else:
            print("Invalid index")

    def view_income(self):
        print("Income:")
        for i, income in enumerate(self.income, start=1):
            print(f"{i}: {income}")

    def calculate_avg_revenue(self):
        if not self.income:
            return 0
        avg_revenue = sum(self.income) / len(self.income)
        return avg_revenue

    def calculate_total_income(self):
        total_income = sum(self.income)
        return total_income

    def add_outcome(self, total_outcome):
        if total_outcome > self.max_outcome:
            print("Expenses exceed maximum limit!")
        else:
            self.outcome.append(float(total_outcome))
            print("Expense added successfully.")

    def remove_outcome(self, index):
        if 0 <= index < len(self.outcome):
            removed_outcome = self.outcome.pop(index)
            print(f"Expense {removed_outcome} removed successfully.")
        else:
            print("Invalid index.")

    def edit_outcome(self, index, new_amount):
        if 0 <= index < len(self.outcome):
            self.outcome[index] = new_amount
            print("Expense edited successfully.")
        else:
            print("Invalid index.")

    def view_outcome(self):
        print("Outcome:")
        for i, outcome in enumerate(self.outcome, start=1):
            print(f"{i}: {outcome}")

    def calculate_avg_expenditures(self):
        if not self.outcome:
            return 0
        avg_expenditures = int (sum(self.outcome) / len(self.outcome))
        return avg_expenditures

    def calculate_total_outcome(self):
        total_outcome = int (sum(self.outcome))
        return total_outcome
    
    def calculate_total_money(self):
        total_income = self.calculate_total_income()
        total_outcome = self.calculate_total_outcome()
        total_money = total_income - total_outcome
        return total_money

if __name__ == "__main__":
    money = Money()

    while True:
        print("\nMenu:")
        print("1. Add Income")
        print("2. Remove Income")
        print("3. Edit Income")
        print("4. View Income")
        print("5. Calculate Average Revenue")
        print("6. Calculate Total Income")
        print("7. Add Outcome")
        print("8. Remove Outcome")
        print("9. Edit Outcome")
        print("10. View Outcome")
        print("11. Calculate Average Expenditures")
        print("12. Calculate Total Outcome")
        print("13. Calculate Total Money")
        print("14. Finish")

        choice = input("Choose: 1/2/3/4/5/6/7/8/9/10/11/12/13/14: ")

        if choice == "1":
            income = input("Enter the income: ")
            money.add_income(income)
        elif choice == "2":
            index = int(input("Enter the index of the income to remove: "))
            money.remove_income(index)
        elif choice == "3":
            index = int(input("Enter the index of the income to edit: "))
            new_income = input("Enter the new income: ")
            money.edit_income(index, new_income)
        elif choice == "4":
            money.view_income()
        elif choice == "5":
            avg_revenue = money.calculate_avg_revenue()
            print(f"Average monthly incomes : {avg_revenue}")
        elif choice == "6":
            total_income = money.calculate_total_income()
            print(f"Total income : {total_income}")
        elif choice == "7":
            outcome = float(input("Enter the expenditure amount : "))
            money.add_outcome(outcome)
        elif choice == "8":
            index = int(input("Enter the index of the expense to remove: "))
            money.remove_outcome(index)
        elif choice == "9":
            index = int(input("Enter the index of the expense to edit: "))
            new_amount = float(input("Enter the new amount: "))
            money.edit_outcome(index, new_amount)
        elif choice == "10":
            money.view_outcome()
        elif choice == "11":
            avg_expenditures = money.calculate_avg_expenditures()
            print(f"Average monthly expenses : {avg_expenditures}")
        elif choice == "12":
            total_outcome = money.calculate_total_outcome()
            print(f"Total outcome : {total_outcome}")
        elif choice == "13":
            total_money = money.calculate_total_money()
            print(f"Total money : {total_money}")
        elif choice == "14":
            print("Program finished.")
            break
        else:
            print("Invalid choice.")