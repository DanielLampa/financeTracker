from app.views import MainView
from app.database import Database  # Import Database from the new file


class MainController:

    def __init__(self, root):
        self.root = root
        self.main_view()

    def main_view(self):
        data = Database()
        total_income = data.get_total_income()
        total_expenses = data.get_total_expenses()
        self.main_view = MainView(master=self.root, controller=self, income=total_income, expenses=total_expenses)
        self.main_view.pack()


    def show_income_view(self):
        pass
    def show_expense_view(self):
        pass
    def show_report_view(self):
        pass


