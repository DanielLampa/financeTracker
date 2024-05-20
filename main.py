import tkinter as tk
from app.controllers import MainController

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.controller = MainController(root=self)

    def show_income_view(self):
        self.controller.show_income_view()

    def show_expense_view(self):
        self.controller.show_expense_view()

    def show_report_view(self):
        self.controller.show_report_view()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
