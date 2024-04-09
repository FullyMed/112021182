 import pprint

class YearEndOverview:
    def __init__(self, initial_deposit):
        self.capital = initial_deposit
        self.yearlyprofits = []
    
    def calculate_profit(self, sales, expenses):
        profit = sales - expenses
        return profit
    
    def calculate_yearly_profit(self):
        for i in range(12):
            sales = int(input("Enter sales for the month: "))
            expenses = int(input("Enter expenses for the month: "))
            profit = self.calculate_profit(sales, expenses)
            self.yearlyprofits.append(profit)
            print(profit)
    
    def display_transactions(self):
        pprint.pprint(self.yearlyprofits)

    def check_profit(self):
        for profit in self.yearlyprofits:
            match profit:
                case 4000:
                    print("New margins need to be implemented")
                case 5000:
                    print("We're doing great, but we can do better")
                case 6000:
                    print("We're smashing it! Consider investing in other markets.")
                case _:
                    print("Your profit is within the normal range.")

overview = YearEndOverview(2000)
overview.calculate_yearly_profit()
overview.display_transactions()
overview.check_profit()
overview.check_profit(self):
