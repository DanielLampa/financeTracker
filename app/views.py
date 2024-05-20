import tkinter as tk

class MainView(tk.Frame):
    def __init__(self, master=None, controller=None, income=0, expenses=0):
        super().__init__(master)
        self.master = master
        self.controller = controller
        self.income = income
        self.expenses = expenses
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Personal Finance Manager")
        self.label.pack()

        self.label = tk.Label(self, text=f"TOTAL INCOME: {self.income}")
        self.label.pack()

        self.label = tk.Label(self, text=f"TOTAL EXPENSES: {self.expenses}")
        self.label.pack()

        self.income_button = tk.Button(self, text="Add Income", command=self.controller.show_income_view)
        self.income_button.pack()

        self.expense_button = tk.Button(self, text="Add Expense", command=self.controller.show_expense_view)
        self.expense_button.pack()

        self.report_button = tk.Button(self, text="Generate Report", command=self.controller.show_report_view)
        self.report_button.pack()

class IncomeView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Add Income")
        self.label.pack()
        self.amount_label = tk.Label(self, text="Amount:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack()
        self.date_label = tk.Label(self, text="Date:")
        self.date_label.pack()
        self.date_entry = tk.Entry(self)
        self.date_entry.pack()
        self.description_label = tk.Label(self, text="Description:")
        self.description_label.pack()
        self.description_entry = tk.Entry(self)
        self.description_entry.pack()
        self.save_button = tk.Button(self, text="Save", command=self.save_income)
        self.save_button.pack()
        self.save_button = tk.Button(self, text="Back")
        self.save_button.pack()

    def save_income(self):
        # Logic to save income
        pass

class ExpenseView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Add Expense")
        self.label.pack()
        self.amount_label = tk.Label(self, text="Amount:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack()
        self.date_label = tk.Label(self, text="Date:")
        self.date_label.pack()
        self.date_entry = tk.Entry(self)
        self.date_entry.pack()
        self.description_label = tk.Label(self, text="Description:")
        self.description_label.pack()
        self.description_entry = tk.Entry(self)
        self.description_entry.pack()
        self.save_button = tk.Button(self, text="Save", command=self.save_expense)
        self.save_button.pack()

    def save_expense(self):
        # Logic to save expense
        pass

class ReportView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Generate Report")
        self.label.pack()
        # Logic to display report
        pass
