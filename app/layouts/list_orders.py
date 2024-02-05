import flet as ft
from app.components.orders import Order
from app.components.new_order import NewOrder


class ListOrder(ft.UserControl):

    def __init__(self):
        super().__init__()

    def build(self):
        self.orders = ft.Column()


        return ft.Column(
            controls=[
                ft.Column(
                    spacing=25,
                    controls=[
                        NewOrder(self.add_clicked),
                        self.orders,
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ],
                ),
            ],
        )

    async def add_clicked(self, e):
        order = Order(
            status="Teste",
            user_name="Nome test",
            items=["Brigadeiro teste"],
            tag="FURB",
            price=999,
        )

        self.orders.controls.append(order)
        # self.new_order.value = ""

        await self.update_async()

    async def update_async(self):
        await super().update_async()
