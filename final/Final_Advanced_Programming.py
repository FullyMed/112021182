import re
import csv
import json
import pandas as pd
import mysql.connector
from mysql.connector import Error
from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class MySQLDatabase:
    def __init__(self, host: str, user: str, password: str, database: str):
        self.conn = None
        try:
            self.conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            if self.conn.is_connected():
                print('Connected to MySQL database')
        except Error as e:
            print(f"Error: {e}")
            messagebox.showerror("Database Connection Error", f"Failed to connect to MySQL : {e}")
            self.conn = None

    def create_tables(self):
        if not self.conn:
            print("Connection not established.")
            return
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS income (
            id INT AUTO_INCREMENT PRIMARY KEY,
            amount FLOAT,
            timestamp DATETIME
        )""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            amount FLOAT,
            timestamp DATETIME,
            category VARCHAR(255)
        )""")
        self.conn.commit()
        cursor.close()

    def insert_income(self, amount: float, timestamp: datetime):
        if not self.conn:
            print("Connection not established.")
            return
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO income (amount, timestamp) VALUES (%s, %s)", (amount, timestamp))
        self.conn.commit()
        cursor.close()

    def insert_expense(self, amount: float, timestamp: datetime, category: str):
        if not self.conn:
            print("Connection not established.")
            return
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO expenses (amount, timestamp, category) VALUES (%s, %s, %s)", (amount, timestamp, category))
        self.conn.commit()
        cursor.close()

    def fetch_all_income(self):
        if not self.conn:
            print("Connection not established.")
            return []
        cursor = self.conn.cursor()
        cursor.execute("SELECT amount, timestamp FROM income")
        result = cursor.fetchall()
        cursor.close()
        return result

    def fetch_all_expenses(self):
        if not self.conn:
            print("Connection not established.")
            return []
        cursor = self.conn.cursor()
        cursor.execute("SELECT amount, timestamp, category FROM expenses")
        result = cursor.fetchall()
        cursor.close()
        return result

    def close(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()

@dataclass
class Transaction:
    amount: float
    timestamp: datetime

@dataclass
class Expense(Transaction):
    category: str

@dataclass
class MoneyData:
    income: pd.DataFrame
    expenses: pd.DataFrame
    max_expense: float
    db: MySQLDatabase

    def __init__(self, max_expense: float, db: MySQLDatabase):
        self.income = pd.DataFrame(columns=["amount", "timestamp"])
        self.expenses = pd.DataFrame(columns=["amount", "timestamp", "category"])
        self.max_expense = max_expense
        self.db = db
        self.db.create_tables()
        self.load_from_db()

    def add_income(self, income_amount: float) -> None:
        timestamp = datetime.now()
        new_income = pd.DataFrame([[income_amount, timestamp]], columns=["amount", "timestamp"])
        self.income = pd.concat([self.income, new_income], ignore_index=True)
        self.db.insert_income(income_amount, timestamp)

    def add_expense(self, expense_amount: float, category: str) -> str:
        if expense_amount > self.max_expense:
            return "Expenses exceed maximum limit !"
        else:
            timestamp = datetime.now()
            new_expense = pd.DataFrame([[expense_amount, timestamp, category]], columns=["amount", "timestamp", "category"])
            self.expenses = pd.concat([self.expenses, new_expense], ignore_index=True)
            self.db.insert_expense(expense_amount, timestamp, category)
            return ""

    def load_from_db(self):
        income_data = self.db.fetch_all_income()
        if income_data:
            self.income = pd.DataFrame(income_data, columns=["amount", "timestamp"])

        expense_data = self.db.fetch_all_expenses()
        if expense_data:
            self.expenses = pd.DataFrame(expense_data, columns=["amount", "timestamp", "category"])

    def remove_income(self, index: int) -> None:
        if 0 <= index < len(self.income):
            self.income = self.income.drop(index).reset_index(drop=True)

    def edit_income(self, index: int, new_income: float) -> None:
        if 0 <= index < len(self.income):
            self.income.at[index, "amount"] = new_income

    def view_income(self) -> List[str]:
        return self.income.to_string(index=False).split("\n")

    def calculate_avg_revenue(self) -> float:
        if self.income.empty:
            return 0
        return self.income["amount"].mean()

    def calculate_total_income(self) -> float:
        return self.income["amount"].sum()

    def remove_expense(self, index: int) -> None:
        if 0 <= index < len(self.expenses):
            self.expenses = self.expenses.drop(index).reset_index(drop=True)

    def view_expenses(self) -> List[str]:
        return self.expenses.to_string(index=False).split("\n")

    def calculate_avg_expenditures(self) -> Dict[str, float]:
        return self.expenses.groupby("category")["amount"].mean().to_dict()

    def calculate_total_expense(self) -> float:
        return self.expenses["amount"].sum()

    def calculate_total_money(self) -> float:
        total_income = self.calculate_total_income()
        total_expense = self.calculate_total_expense()
        return total_income - total_expense

    def save_to_file(self, filename="money_data.json"):
        data = {
            "Income": self.income.to_dict(orient="records"),
            "Expenses": self.expenses.to_dict(orient="records"),
            "Max_expense": self.max_expense
        }
        with open(filename, 'w') as file:
            json.dump(data, file)
        print(f"Data saved to {filename}")

    def load_from_file(self, filename="money_data.json"):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.max_expense = data["Max_expense"]
                self.income = pd.DataFrame(data["Income"])
                self.expenses = pd.DataFrame(data["Expenses"])
            print(f"Data loaded from {filename}")
        except FileNotFoundError:
            print("No previous data found, starting fresh.")


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


class MoneyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Money Management System")

        max_expense = simpledialog.askfloat("Maximum Expense", "Enter the maximum spending limit per month :")
        if max_expense is None:
            messagebox.showwarning("Error", "Maximum expense is required.")
            self.root.destroy()
            return

        self.db = MySQLDatabase(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="money_management"
        )

        if self.db.conn is None:
            self.root.destroy()
            return

        self.data = MoneyData(max_expense, self.db)
        self.income = None
        self.tax_rates_percentage = None
        self.needs_percentage = None
        self.money_percentage_for_wants = None

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Button(frame, text="Add Income", command=self.add_income).grid(row=0, column=0, sticky=tk.W)
        ttk.Button(frame, text="Remove Income", command=self.remove_income).grid(row=0, column=1, sticky=tk.W)
        ttk.Button(frame, text="Edit Income", command=self.edit_income).grid(row=0, column=2, sticky=tk.W)
        ttk.Button(frame, text="View Income", command=self.view_income).grid(row=0, column=3, sticky=tk.W)
        ttk.Button(frame, text="Calculate Average Revenue", command=self.calculate_avg_revenue).grid(row=2, column=0, sticky=tk.W)
        ttk.Button(frame, text="Calculate Total Income", command=self.calculate_total_income).grid(row=2, column=1, sticky=tk.W)
        ttk.Button(frame, text="Add Expense", command=self.add_expense).grid(row=3, column=0, sticky=tk.W)
        ttk.Button(frame, text="Remove Expense", command=self.remove_expense).grid(row=3, column=1, sticky=tk.W)
        ttk.Button(frame, text="View Expenses", command=self.view_expenses).grid(row=3, column=2, sticky=tk.W)
        ttk.Button(frame, text="Calculate Average Expenditures", command=self.calculate_avg_expenditures).grid(row=4, column=0, sticky=tk.W)
        ttk.Button(frame, text="Calculate Total Expense", command=self.calculate_total_expense).grid(row=4, column=1, sticky=tk.W)
        ttk.Button(frame, text="Calculate Total Money", command=self.calculate_total_money).grid(row=5, column=0, sticky=tk.W)
        ttk.Button(frame, text="Save to File", command=self.save_to_file).grid(row=5, column=1, sticky=tk.W)
        ttk.Button(frame, text="Load from File", command=self.load_from_file).grid(row=5, column=2, sticky=tk.W)
        ttk.Button(frame, text="Exit", command=self.root.quit).grid(row=5, column=3, sticky=tk.W)

    def add_income(self):
        income_amount = simpledialog.askfloat("Add Income", "Enter the income amount :")
        if income_amount is not None:
            self.data.add_income(income_amount)
            messagebox.showinfo("Income Added", "Income added successfully !")

    def remove_income(self):
        index = simpledialog.askinteger("Remove Income", "Enter the index of the income to remove :")
        if index is not None:
            self.data.remove_income(index)
            messagebox.showinfo("Income Removed", "Income removed successfully !")

    def edit_income(self):
        index = simpledialog.askinteger("Edit Income", "Enter the index of the income to edit :")
        if index is not None:
            new_income = simpledialog.askfloat("Edit Income", "Enter the new income amount :")
            if new_income is not None:
                self.data.edit_income(index, new_income)
                messagebox.showinfo("Income Edited", "Income edited successfully !")

    def view_income(self):
        income_view = self.data.view_income()
        messagebox.showinfo("View Income", "\n".join(income_view))

    def calculate_avg_revenue(self):
        avg_revenue = self.data.calculate_avg_revenue()
        messagebox.showinfo("Average Revenue", f"The average revenue is : {avg_revenue:.2f}")

    def calculate_total_income(self):
        total_income = self.data.calculate_total_income()
        messagebox.showinfo("Total Income", f"The total income is : {total_income:.2f}")

    def add_expense(self):
        expense_amount = simpledialog.askfloat("Add Expense", "Enter the expense amount :")
        if expense_amount is not None:
            category = simpledialog.askstring("Add Expense", "Enter the expense category :")
            if category is not None:
                message = self.data.add_expense(expense_amount, category)
                if message:
                    messagebox.showinfo("Add Expense", message)
                else:
                    messagebox.showinfo("Expense Added", "Expense added successfully !")

    def remove_expense(self):
        index = simpledialog.askinteger("Remove Expense", "Enter the index of the expense to remove :")
        if index is not None:
            self.data.remove_expense(index)
            messagebox.showinfo("Expense Removed", "Expense removed successfully !")

    def view_expenses(self):
        expenses_view = self.data.view_expenses()
        messagebox.showinfo("View Expenses", "\n".join(expenses_view))

    def calculate_avg_expenditures(self):
        avg_expenditures = self.data.calculate_avg_expenditures()
        messagebox.showinfo("Average Expenditures", "\n".join([f"{k}: {v:.2f}" for k, v in avg_expenditures.items()]))

    def calculate_total_expense(self):
        total_expense = self.data.calculate_total_expense()
        messagebox.showinfo("Total Expense", f"The total expense is: {total_expense:.2f}")

    def calculate_total_money(self):
        total_money = self.data.calculate_total_money()
        messagebox.showinfo("Total Money", f"The total money is : {total_money:.2f}")

    def save_to_file(self):
        self.data.save_to_file()
        messagebox.showinfo("Save to File", "Data saved to file successfully !")

    def load_from_file(self):
        self.data.load_from_file()
        messagebox.showinfo("Load from File", "Data loaded from file successfully !")

    def calculate_budget_allocation(self):
        self.income = simpledialog.askfloat("Budget Allocation", "Enter the monthly salary :")
        self.tax_rates_percentage = simpledialog.askfloat("Budget Allocation", "Enter your taxes (in percentage) :")
        self.needs_percentage = simpledialog.askfloat("Budget Allocation", "Enter your needs (in percentage) :")
        self.money_percentage_for_wants = simpledialog.askfloat("Budget Allocation", "Enter the percentage for wants (in percentage) :")

        if self.income is not None and self.tax_rates_percentage is not None and self.needs_percentage is not None and self.money_percentage_for_wants is not None:
            savings_recommendation = SavingsRecommendation(self.income)
            taxes = savings_recommendation.percentage_money_for_taxes(self.tax_rates_percentage)
            needs = savings_recommendation.percentage_money_for_needs(self.needs_percentage)
            wants = savings_recommendation.percentage_money_for_wants(self.money_percentage_for_wants)

            message = (f"Budget Allocation :\n"
                       f"  - Taxes : ${taxes:.2f}\n"
                       f"  - Needs : ${needs:.2f}\n"
                       f"  - Wants : ${wants:.2f}\n"
                       f"Remaining Money after expenses : ${self.income - (taxes + needs + wants):.2f}")
            messagebox.showinfo("Budget Allocation", message)
        else:
            messagebox.showwarning("Error", "Please fill in all fields.")

    def store_data(self):
        if self.income is not None and self.tax_rates_percentage is not None and self.needs_percentage is not None and self.money_percentage_for_wants is not None:
            customer_data = [
                ["Income", "Taxes", "Needs", "Wants"],
                [self.income, self.tax_rates_percentage, self.needs_percentage, self.money_percentage_for_wants]
            ]
            StoreData.store_to_csv(customer_data, 'customer_data.csv')
            messagebox.showinfo("Success", "Data stored successfully !")
        else:
            messagebox.showwarning("Error", "Please calculate the budget allocation first.")


if __name__ == "__main__":
    root = tk.Tk()
    app = MoneyApp(root)
    root.mainloop()