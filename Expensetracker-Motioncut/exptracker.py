import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        self.expenses = []

        # Create and pack UI elements
        self.label_amount = tk.Label(root, text="Amount:")
        self.label_amount.pack()
        self.entry_amount = tk.Entry(root)
        self.entry_amount.pack()

        self.label_description = tk.Label(root, text="Description:")
        self.label_description.pack()
        self.entry_description = tk.Entry(root)
        self.entry_description.pack()

        self.label_category = tk.Label(root, text="Category:")
        self.label_category.pack()
        self.entry_category = tk.Entry(root)
        self.entry_category.pack()

        self.button_submit = tk.Button(root, text="Submit", command=self.submit_expense)
        self.button_submit.pack()

    def submit_expense(self):
        amount = self.entry_amount.get()
        description = self.entry_description.get()
        category = self.entry_category.get()

        if not amount or not description or not category:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a numeric value.")
            return

        expense = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "amount": amount,
            "description": description,
            "category": category
        }

        self.expenses.append(expense)
        self.save_expenses()
        messagebox.showinfo("Success", "Expense added successfully.")

        self.entry_amount.delete(0, tk.END)
        self.entry_description.delete(0, tk.END)
        self.entry_category.delete(0, tk.END)

    def save_expenses(self):
        with open("expenses.json", "w") as file:
            json.dump(self.expenses, file)

    def load_expenses(self):
        try:
            with open("expenses.json", "r") as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            # File doesn't exist yet, so we'll initialize an empty list of expenses
            self.expenses = []

def main():
    root = tk.Tk()
    app = ExpenseTracker(root)
    app.load_expenses()
    root.mainloop()

if __name__ == "__main__":
    main()
