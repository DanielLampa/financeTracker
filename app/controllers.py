from app.views import MainView, IncomeView, ExpenseView, ReportView
from app.models import Database


class MainController:
    def __init__(self, root):
        self.root = root
        self.db = Database()  # Initialize the database connection
        self.update_main_view()

    def update_main_view(self):
        total_income = self.db.get_total_income()
        total_expenses = self.db.get_total_expenses()
        self.main_view = MainView(master=self.root, controller=self, income=total_income, expenses=total_expenses)
        self.main_view.pack()

    def show_income_view(self):
        if self.income_view:
            self.income_view.destroy()
        self.income_view = IncomeView(master=self.root)
        self.main_view.pack_forget()
        self.income_view.pack()

    def show_expense_view(self):
        if self.expense_view:
            self.expense_view.destroy()
        self.expense_view = ExpenseView(master=self.root)
        self.main_view.pack_forget()
        self.expense_view.pack()

    def show_report_view(self):
        if self.report_view:
            self.report_view.destroy()
        self.report_view = ReportView(master=self.root)
        self.main_view.pack_forget()
        self.report_view.pack()
