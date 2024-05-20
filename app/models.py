import sqlite3
class Database:
    def __init__(self):
        self.db_connection = sqlite3.connect("finance.db")
        self.db_cursor = self.db_connection.cursor()

    def get_total_expenses(self):
        self.db_cursor.execute("SELECT SUM(amount) FROM expense")
        # Fetch the result of the query
        total_expenses = self.db_cursor.fetchone()[0]
        # If total_expenses is None, set it to 0
        if total_expenses is None:
            total_expenses = 0
        return total_expenses
    def get_total_income(self):
        self.db_cursor.execute("SELECT SUM(amount) FROM income")
        # Fetch the result of the query
        total_income = self.db_cursor.fetchone()[0]
        # If total_expenses is None, set it to 0
        if total_income is None:
            total_income = 0
        return total_income

    def check_balance(self):
        income=self.get_total_income()
        expense=self.get_total_expenses()
        return (income - expense)

class Transaction(Database):
    def __init__(self, amount, date, description):
        super().__init__()
        self.amount = amount
        self.date = date
        self.description = description

    def add_income(self):
        # Execute the INSERT query to add data to the income table
        self.db_cursor.execute("INSERT INTO income (amount, date, description) VALUES (?, ?, ?)",
                               (self.amount, self.date, self.description))
        self.db_connection.commit()

    def add_expenses(self):
        if(self.amount>self.check_balance()):
            return print("Insufficient funds!!")
        else:
            self.db_cursor.execute("INSERT INTO expense (amount, date, description) VALUES (?, ?, ?)",
                               (self.amount, self.date, self.description))
            self.db_connection.commit()





