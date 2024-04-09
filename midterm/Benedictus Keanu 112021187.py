class Money:
    def __init__(self):
        self.income = []
        
    def add_income(self, income):
        self.income.append(income)
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
        for i, income in enumerate(self.income):
            print(f"{i}: {income}")

money = Money()

while True:
    print("\nMenu:")
    print("1. Add Income")
    print("2. Remove Income")
    print("3. Edit Income")
    print("4. View Income")
    print("5. Exit")
    
    choice = input("Choose: 1/2/3/4/5: ")

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
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")