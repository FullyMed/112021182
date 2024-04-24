import matplotlib.pyplot as plt

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

    def total_income(self):
        return sum(self.income)

    def average_income(self):
        if self.income:
            return sum(self.income) / len(self.income)
        else:
            return 0

    def max_income(self):
        if self.income:
            return max(self.income)
        else:
            return None

    def min_income(self):
        if self.income:
            return min(self.income)
        else:
            return None

    def plot_income_distribution(self):
        plt.hist(self.income, bins=10, color='green', edgecolor='black')
        plt.xlabel('Income')
        plt.ylabel('Frequency')
        plt.title('Income Distribution')
        plt.grid(True)
        plt.show()

money = Money()

while True:
    print("\nMenu:")
    print("1. Add Income")
    print("2. Remove Income")
    print("3. Edit Income")
    print("4. View Income")
    print("5. Calculate Statistics")
    print("6. Plot Income Distribution")
    print("7. Exit")

    choice = input("Choose: 1/2/3/4/5/6/7: ")

    if choice == "1":
        income = float(input("Enter the income: "))
        money.add_income(income)
    elif choice == "2":
        index = int(input("Enter the index of the income to remove: "))
        money.remove_income(index)
    elif choice == "3":
        index = int(input("Enter the index of the income to edit: "))
        new_income = float(input("Enter the new income: "))
        money.edit_income(index, new_income)
    elif choice == "4":
        money.view_income()
    elif choice == "5":
        print(f"Total Income: {money.total_income()}")
        print(f"Average Income: {money.average_income()}")
        print(f"Maximum Income: {money.max_income()}")
        print(f"Minimum Income: {money.min_income()}")
    elif choice == "6":
        money.plot_income_distribution()
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3, 4, 5, 6, or 7.")
