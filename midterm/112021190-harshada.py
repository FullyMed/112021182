class SavingsRecommendation:
    def __init__(self, income):
        self.income = income

    def calculate_budget_allocation(self):
        needs_percentage = 0.5
        wants_percentage = 0.3
        savings_percentage = 0.2

        needs = self.income * needs_percentage
        wants = self.income * wants_percentage
        savings = self.income * savings_percentage

        return f"Allocate {needs_percentage*100}% of your income to needs (${needs:.2f}), {wants_percentage*100}% to wants (${wants:.2f}), and {savings_percentage*100}% to savings (${savings:.2f})."

def main():
    # Input monthly salary
    income = float(input("Enter your monthly salary: "))

    savings_recommendation = SavingsRecommendation(income)

    while True:
        print("\nMenu:")
        print("1. Calculate Budget Allocation")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print(savings_recommendation.calculate_budget_allocation())
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
