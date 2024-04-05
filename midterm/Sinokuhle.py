class YearEndOverview:
    def __init__(self,initial_deposit):
        self.sales=initial_deposit
        self.transaction=[]
    def profit(sales,expenses):
    sales=float(input())
    expenses=float(input())
    profit=sales-expenses
    return profit 
match profit:
    case 4000:
        print("New margins need to be implemented")
    case 5000:
        print("We're doing great,but we can do better")
    case 6000:
        print("We're smashing it! Consider investing in other markets.")   
