import unittest
from app.models import Income, Expense, Budget


class TestModels(unittest.TestCase):
    def test_income_creation(self):
        income = Income(1000, "2024-05-20", "Salary")
        self.assertEqual(income.amount, 1000)
        self.assertEqual(income.date, "2024-05-20")
        self.assertEqual(income.description, "Salary")

    def test_budget(self):
        budget = Budget(5000)
        expense = Expense(100, "2024-05-21", "Groceries")
        budget.add_expense(expense)
        self.assertEqual(budget.get_total_expenses(), 100)
