import re
import csv


class SavingsRecommendation:
    def __init__(self, income):
        self.income = income

    def percentage_money_for_taxes(self, tax_rates_percentage):
        return self.income * (tax_rates_percentage / 100)

    def percentage_money_for_needs(self, needs_percentage):
        return self.income * (needs_percentage / 100)

    def percentage_money_for_wants(self, money_percentage_for_wants):
        return self.income * (money_percentage_for_wants / 100)


class StoreData:
    @staticmethod
    def store_to_csv(data, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"Data stored into {filename}")


def main():
    while True:
        income = input("Enter the monthly salary: ")
        if re.match(r'^\d+(\.\d+)?$', income):
            income = float(income)
            break
        else:
            print("Please enter a valid number.")

    while True:
        tax_rates_percentage = input("Enter your taxes (in percentage): ")
        if re.match(r'^\d+(\.\d+)?$', tax_rates_percentage):
            tax_rates_percentage = float(tax_rates_percentage)
            break
        else:
            print("Please enter a valid number.")

    while True:
        needs_percentage = input("Enter your needs (in percentage): ")
        if re.match(r'^\d+(\.\d+)?$', needs_percentage):
            needs_percentage = float(needs_percentage)
            break
        else:
            print("Please enter a valid number.")

    while True:
        money_percentage_for_wants = input("Enter the percentage for wants (in percentage): ")
        if re.match(r'^\d+(\.\d+)?$', money_percentage_for_wants):
            money_percentage_for_wants = float(money_percentage_for_wants)
            break
        else:
            print("Please enter a valid number.")

    savings_recommendation = SavingsRecommendation(income)
    store_data = StoreData()

    while True:
        print("\nMenu:")
        print("1. Calculate Budget Allocation")
        print("2. Store the data")
        print("3. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                taxes = savings_recommendation.percentage_money_for_taxes(tax_rates_percentage)
                needs = savings_recommendation.percentage_money_for_needs(needs_percentage)
                wants = savings_recommendation.percentage_money_for_wants(money_percentage_for_wants)
                print("Budget Allocation:")
                print(f"  - Taxes: ${taxes:.2f}")
                print(f"  - Needs: ${needs:.2f}")
                print(f"  - Wants: ${wants:.2f}")
                total_expenses = taxes + needs + wants
                remaining_money = income - total_expenses
                print(f"Remaining Money after expenses: ${remaining_money:.2f}")

            case '2':
                print("Store the data")
                customer_data = [
                    ["Taxes", "Needs", "Wants"],
                    [tax_rates_percentage, needs_percentage, money_percentage_for_wants]
                ]
                store_data.store_to_csv(customer_data, 'customer_data.csv')

            case '3':
                print("Exiting the program.")
                return

            case _:
                print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
