import flet as ft
from app.layouts.list_orders import ListOrder


class CandyApp(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.orders = ListOrder()

    def build(self):
        return self.orders
