import flet as ft
from app.components.orders.orders import Order
from app.components.orders.new_order import NewOrder


class ListOrder(ft.UserControl):

    def __init__(self):
        super().__init__()

    def build(self):
        # self.orders = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self.orders = ft.ListView()

        return ft.Column(
            controls=[
                self.__mount_new_order_button(),
                self.__mount_orders(),
            ],
        )

    def __mount_new_order_button(self) -> ft.Column:
        return ft.Column(
            spacing=25,
            controls=[
                NewOrder(new_order_function=self.add_clicked),
            ],
        )

    def __mount_orders(self) -> ft.Row:
        return ft.Container(
            content=ft.Column(
                alignment=ft.MainAxisAlignment.START,
                controls=[
                    ft.ElevatedButton(
                        tooltip="Ver todos os pedidos",
                        bgcolor=ft.colors.WHITE,
                        on_click=self.show_orders,
                        content=ft.Container(
                            content=ft.Row(
                                [
                                    ft.Text(value="Pedidos Pendentes", size=18),
                                    ft.Image(
                                        src=f"/svgs/arrow-next-svgrepo-com.svg"
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                expand=True,
                                spacing=10,
                            ),
                        ),
                    ),
                    self.orders
                    # ft.Row(
                    #     controls=[
                    #     alignment=ft.MainAxisAlignment.CENTER,
                    #     vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    # ),
                ],
            ),
            bgcolor=ft.colors.WHITE,
            padding=16,
            alignment=ft.alignment.center,
            border_radius=16,
            border=ft.border.only(
                bottom=ft.border.BorderSide(width=2, color=ft.colors.GREY_500)
            ),
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

    async def show_orders(self, e):
        print("nova view")

    async def update_async(self):
        await super().update_async()
