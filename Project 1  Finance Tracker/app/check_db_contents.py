from app.database import Database
from app.models import Transaction


data=Database()
print(data.get_total_expenses())
print(data.get_total_income())
print(data.check_balance())


class Data:
    def __init__(self):
        pass

    def display(self):
        db = Database()
        print(db.get_total_expenses())
        print(db.get_total_income())
        print(db.check_balance())


data_instance = Data()
data_instance.display()

trans1=Transaction(200,"12.11.22","sfdasfd")
trans1.add_income()

