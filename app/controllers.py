from app.views import MainView, IncomeView, ExpenseView, ReportView
from app.models import Database

class MainController:
    def __init__(self, root):
        self.root = root
        self.database = Database()

        # Fetch initial data
        self.update_financial_data()

        # Initialize main view
        self.main_view = MainView(master=self.root, controller=self, income=self.income, expenses=self.expenses)
        self.main_view.pack()

        self.income_view = None
        self.expense_view = None
        self.report_view = None

    def update_financial_data(self):
        self.income = self.database.get_total_income()
        self.expenses = self.database.get_total_expenses()


    def show_income_view(self):
        # Destroy current view if it exists
        if self.income_view:
            self.income_view.destroy()
        # Create and show the income view
        self.income_view = IncomeView(master=self.root)
        self.main_view.pack_forget()  # Hide main view
        self.income_view.pack()# Show income view

    def show_expense_view(self):
        # Destroy current view if it exists
        if self.expense_view:
            self.expense_view.destroy()
        # Create and show the expense view
        self.expense_view = ExpenseView(master=self.root)
        self.main_view.pack_forget()  #Hide main view
        self.expense_view.pack()      #Show expense view

    def show_report_view(self):
        # Destroy current view if it exists
        if self.report_view:
            self.report_view.destroy()
        # Create and show the report view
        self.report_view = ReportView(master=self.root)
        self.main_view.pack_forget()  # Hide main view
        self.report_view.pack()       # Show report view
