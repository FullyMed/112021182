class Money_Management:
    def __init__(self, max_outcome):
        self.outcome = []
        self.max_outcome = max_outcome

    def add_outcome(self, total_outcome):
        if total_outcome > self.max_outcome:
            print("Expenses exceed maximum limit!")
        else:
            self.outcome.append(total_outcome)
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

    def calculate_avg(self):
        if not self.outcome:
            return 0
        avg = sum(self.outcome) / len(self.outcome)
        return avg

def main():
    maximum_expense_limit = float(input("Enter the maximum spending limit per month : "))
    money_manager = Money_Management(maximum_expense_limit)

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. Edit Expense")
        print("4. Calculate Average Expenditures")
        print("5. Finish")

        choice = input("Choose (1/2/3/4/5): ")

        if choice == "1":
            total_outcome = float(input("Enter the expenditure amount : "))
            money_manager.add_outcome(total_outcome)
        elif choice == "2":
            index = int(input("Enter the index of the expense to remove: "))
            money_manager.remove_outcome(index)
        elif choice == "3":
            index = int(input("Enter the index of the expense to edit: "))
            new_amount = float(input("Enter the new amount: "))
            money_manager.edit_outcome(index, new_amount)
        elif choice == "4":
            avg = money_manager.calculate_avg()
            print(f"Average monthly expenses : {avg}")
        elif choice == "5":
            print("Program finished.")
            break
        else:
            print("Try again.")

if __name__ == "__main__":
    main()
