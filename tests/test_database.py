import unittest
from app.models import Income, Expense, Budget


class TestIncome(unittest.TestCase):
    def test_income_creation(self):
        income = Income(500, "2024-05-01", "Salary")
        self.assertEqual(income.amount, 500)
        self.assertEqual(income.date, "2024-05-01")
        self.assertEqual(income.description, "Salary")


class TestExpense(unittest.TestCase):
    def test_expense_creation(self):
        expense = Expense(200, "2024-05-02", "Groceries")
        self.assertEqual(expense.amount, 200)
        self.assertEqual(expense.date, "2024-05-02")
        self.assertEqual(expense.description, "Groceries")


class TestBudget(unittest.TestCase):
    def setUp(self):
        self.budget = Budget()
        self.income1 = Income(1000, "2024-05-01", "Salary")
        self.income2 = Income(500, "2024-05-15", "Freelance Work")
        self.expense1 = Expense(200, "2024-05-02", "Groceries")
        self.expense2 = Expense(300, "2024-05-10", "Utilities")

    def test_add_income(self):
        self.budget.add_income(self.income1)
        self.assertIn(self.income1, self.budget.incomes)

    def test_add_expense(self):
        self.budget.add_expense(self.expense1)
        self.assertIn(self.expense1, self.budget.expenses)

    def test_get_total_income(self):
        self.budget.add_income(self.income1)
        self.budget.add_income(self.income2)
        total_income = self.budget.get_total_income()
        self.assertEqual(total_income, 1500)

    def test_get_total_expenses(self):
        self.budget.add_expense(self.expense1)
        self.budget.add_expense(self.expense2)
        total_expenses = self.budget.get_total_expenses()
        self.assertEqual(total_expenses, 500)

    def test_get_balance(self):
        self.budget.add_income(self.income1)
        self.budget.add_income(self.income2)
        self.budget.add_expense(self.expense1)
        self.budget.add_expense(self.expense2)
        balance = self.budget.get_balance()
        self.assertEqual(balance, 1000)


if __name__ == "__main__":
    unittest.main()

